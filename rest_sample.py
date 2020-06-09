import ssl
import os
from poloniex.client import Trade
from poloniex.client import Market
from poloniex.client import User

context = ssl._create_unverified_context()

# Account Keys
API_KEY = os.environ['KUMEX_SBOX_API_KEY']
SECRET = os.environ['KUMEX_SBOX_SECRET']
API_PASS = os.environ['KUMEX_PASS']
SANDBOX = True

# Fetch MarketData
SYMBOL = 'XBTUSDM'
market = Market(is_sandbox=SANDBOX)

server_time = market.get_server_timestamp()
l3_depth = market.l3_order_book(SYMBOL)
l2_depth = market.l2_order_book(SYMBOL)
klines = market.get_ticker(SYMBOL)


# Trade Functions
trade = Trade(API_KEY, SECRET, API_PASS, is_sandbox=SANDBOX)

order_id = trade.create_limit_order(SYMBOL, 'buy', '1', '30', '8600')
cancel_id = trade.cancel_order(order_id['orderId'])
order_id = trade.create_limit_order(SYMBOL, 'buy', '1', '30', '8600')
cancel_all = trade.cancel_all_limit_order(SYMBOL)

# User Account Functions
user = User(API_KEY, SECRET, API_PASS, is_sandbox=SANDBOX)
address = user.get_withdrawal_quota('XBT')

