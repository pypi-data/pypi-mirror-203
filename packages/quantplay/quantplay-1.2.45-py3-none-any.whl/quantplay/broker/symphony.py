import traceback
import requests
import json

from quantplay.broker.generics.broker import Broker
from quantplay.utils.constant import Constants, timeit
from quantplay.broker.xts_utils.Connect import XTSConnect


class Symphony(Broker):
    source = "WebAPI"

    symphony_secret_key = "symphony_secret_key"
    symphony_app_key = "symphony_app_secret"

    @timeit(MetricName="Symphony:__init__")
    def __init__(self, headers=None, api_secret=None, api_key=None):
        super(Symphony, self).__init__()

        try:
            self.wrapper = XTSConnect(
                apiKey=api_key, secretKey=api_secret, source=self.source
            )
            self.login()

        except Exception as e:
            print(traceback.print_exc())
            raise e

    def login(self):
        response = self.wrapper.interactive_login()
        self.wrapper.marketdata_login()

        self.ClientID = response["result"]["clientCodes"][0]

    def account_summary(self):
        api_response = self.wrapper.get_balance(self.ClientID)

        if not api_response:
            raise Exception(
                "[SYMPHONY_ERROR]: Balance API available for retail API users only, dealers can watch the same on dealer terminal"
            )

        api_response = api_response["result"]["BalanceList"][0]["limitObject"]

        response = {
            # TODO: Get PNL
            "pnl": 0,
            "margin_used": api_response["RMSSubLimits"]["marginUtilized"],
            "margin_available": api_response["RMSSubLimits"]["netMarginAvailable"],
        }

        return response

    def profile(self):
        api_response = self.wrapper.get_profile(self.ClientID)["result"]

        response = {
            "user_id": api_response["ClientId"],
            "full_name": api_response["ClientName"],
            "segments": api_response["ClientExchangeDetailsList"],
        }

        return response

    def orders(self):
        api_response = self.wrapper.get_order_book(self.ClientID)["result"]

        return api_response

    def positions(self):
        api_response = self.wrapper.get_position_daywise(self.ClientID)["result"]

        return api_response

    def get_symbol(self, exchange, symbol, series="EQ"):
        # TODO: Add Futures and Options

        if series not in ["FUTIDX", "EQ"]:
            raise KeyError("INVALID_SERIES: Series not in ['FUTIDX', 'EQ']")

        if series == "EQ":
            response = self.wrapper.get_equity_symbol(
                exchangeSegment=exchange, series=series, symbol=symbol
            )

            if response["type"] == "error":
                raise Exception("[SYMPHONY_ERROR]: " + response["description"])

            return response["result"][0]["ExchangeInstrumentID"]

    def get_exchange(self, exchange):
        # TODO: Confirm Formats
        exchange_code_map = {
            "NSECM": 1,
            "NSEFO": 2,
            "NSECD": 3,
            "BSECM": 11,
            "BSEFO": 12,
        }

        if exchange not in exchange_code_map:
            raise KeyError(
                "INVALID_EXCHANGE: Exchange not in ['NSECM', 'NSEFO', 'NSECD', 'BSECM', 'BSEFO']"
            )

        return exchange_code_map[exchange]

    def get_ltp(self, exchange=None, tradingsymbol=None):
        exchange = self.get_exchange(exchange)
        tradingsymbol = self.get_symbol(exchange, tradingsymbol)

        api_response = self.wrapper.get_quote(
            Instruments=[
                {"exchangeSegment": exchange, "exchangeInstrumentID": tradingsymbol}
            ],
            xtsMessageCode=1512,
            publishFormat="JSON",
        )["result"]

        ltp_json = api_response["listQuotes"][0]

        ltp = json.loads(ltp_json)["LastTradedPrice"]

        return ltp
