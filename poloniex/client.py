from poloniex.market_data.market_data import MarketData
from poloniex.trade.trade import TradeData
from poloniex.user.user import UserData
from poloniex.ws_token.token import GetToken


class Market(MarketData):
    pass


class User(UserData):
    pass


class Trade(TradeData):
    pass


class WSToken(GetToken):
    pass


