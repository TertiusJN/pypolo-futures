
pypolo-futures
===============================
Official Python 3 Wrapper for Poloniex Futures Exchange

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

    #  MarketData
    from poloniex.client import Market
    client = Market()
    # or connect to Sandbox
    # client = Market(is_sandbox=True)

    # get l3_order_book
    l3_depth = client.l3_order_book('XBTUSDM')

    # get l2_order_book
    l2_depth = client.l2_order_book('XBTUSDM')

    # get symbol ticker
    klines = client.get_ticker("XBTUSDM")

    # get symbol ticker
    server_time = client.get_server_timestamp()

    api_key = '<api_key>'
    api_secret = '<api_secret>'
    api_passphrase = '<api_passphrase>'

    # Trade
    from poloniex.client import Trade
    client = Trade(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

    # place a limit buy order
    order_id = client.create_limit_order('XBTUSDM', 'buy', '1', '30', '8600')

    # place a market buy order   Use cautiously
    order_id = client.create_market_order('XBTUSDM', 'buy', '1')

    # cancel limit order
    client.cancel_order('5bd6e9286d99522a52e458de')

    # cancel all limit order
    client.cancel_all_limit_order('XBTUSDM')

    # User
    from poloniex.client import User
    client = User(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

    address = client.get_withdrawal_quota('XBT')

Websockets
----------

.. code:: python

    import asyncio
    from poloniex.client import WSToken
    from poloniex.ws_client import poloniexWSClient


    async def main():
        async def deal_msg(msg):
            if msg['topic'] == '/contractMarket/level2:XBTUSDM':
                print(f'Get XBTUSDM Ticker:{msg["data"]}')
            elif msg['topic'] == '/contractMarket/level3:XBTUSDM':
                print(f'Get XBTUSDM level3:{msg["data"]}')

        # is public
        # client = WsToken()
        # is private
        client = WsToken(key='', secret='', passphrase='')
        # is sandbox
        # client = WSToken(is_sandbox=True)
        ws_client = await poloniexWSClient.create(loop, client, deal_msg, private=False)
        await ws_client.subscribe('/contractMarket/level2:XBTUSDM')
        await ws_client.subscribe('/contractMarket/level3:XBTUSDM')
        while True:
            await asyncio.sleep(60, loop=loop)


    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())