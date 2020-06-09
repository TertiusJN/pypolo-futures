
pypolo-futures
===============================
Python 3 Wrapper for Poloniex Futures Exchange

Features
--------

- Implementation of REST endpoints
- Simple handling of authentication
- Response exception handling
- Implement websockets (note only python3.6+)

Quick Start
-----------

Register an account with `Poloniex <https://www.poloniex.com/ucenter/signup>`_.

To test on the Sandbox  with `Poloniex Sandbox <https://sandbox.poloniex.com>`_.

`Generate an API Key <https://www.poloniex.com/api/create>`_
or `Generate an API Key in Sandbox <https://sandbox.poloniex.com/account/api>`_ and enable it.

.. code:: bash

    pip install pypolo-futures

.. code:: python

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



Websockets
----------

.. code:: python

    import asyncio
    import ssl
    import os

    from poloniex.client import WSToken
    from poloniex.ws_client import PoloFuturesWSClient

    # Account Keys
    context = ssl._create_unverified_context()
    API_KEY = os.environ['KUMEX_SBOX_API_KEY']
    SECRET = os.environ['KUMEX_SBOX_SECRET']
    API_PASS = os.environ['KUMEX_PASS']
    SANDBOX = True


    async def ws_stream():
        async def deal_msg(msg):
            if msg['topic'] == '/contractMarket/level2:XBTUSDM':
                print(f'Get XBTUSDM Ticker: {msg["data"]}')
            elif msg['topic'] == '/contractMarket/execution:XBTUSDM':
                print(f'Last Execution: {msg["data"]}')
            elif msg['topic'] == '/contractMarket/ticker:XBTUSDM':
                print(f'Get XBTUSDM Tick :{msg["data"]}')

        ws = WSToken(API_KEY, SECRET, API_PASS, is_sandbox=SANDBOX)
        ws_client = await PoloFuturesWSClient.create(loop, ws, deal_msg, private=False)

        # Set channel subscriptions
        await ws_client.subscribe('/contractMarket/level2:XBTUSDM')
        await ws_client.subscribe('/contractMarket/execution:XBTUSDM')
        await ws_client.subscribe('/contractMarket/ticker:XBTUSDM')
        while True:
            await asyncio.sleep(0.5, loop=loop)


    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(ws_stream())