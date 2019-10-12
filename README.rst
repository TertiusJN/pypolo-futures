===============================
Welcome to python-kumex-sdk v1.0.6
===============================

.. image:: https://img.shields.io/badge/version-v1.0.6-green
    :target: https://pypi.org/project/python-kumex

.. image:: https://img.shields.io/pypi/l/python-kumex.svg
    :target: https://github.com/grape-cola/kumex-python-sdk/blob/master/LICENSE

.. image:: https://img.shields.io/badge/python-3.6%2B-green
    :target: https://pypi.org/project/python-kumex

.. image:: https://img.shields.io/badge/releases-v1.0.6-green
    :target: https://pypi.org/manage/project/python-kumex/release/1.0.6/

Features
--------

- Implementation of REST endpoints
- Simple handling of authentication
- Response exception handling
- Implement websockets (note only python3.6+)

TODO
----

- websocket

Quick Start
-----------

Register an account with `KuMEX <https://www.kumex.com/ucenter/signup>`_.

To test on the Sandbox  with `KuMEX Sandbox <https://sandbox.kumex.com>`_.

`Generate an API Key <https://www.kumex.com/api/create>`_
or `Generate an API Key in Sandbox <https://sandbox.kucoin.com/account/api>`_ and enable it.

.. code:: bash

    pip install python-kumex

.. code:: python

    #  MarketData
    from kumex.client import Market
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
    from kumex.client import Trade
    client = Trade(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

    # place a limit buy order
    order_id = client.sand_limit_order('XBTUSDM', 'buy', '1', '30', '8600')

    # place a market buy order   Use cautiously
    order_id = client.sand_market_order('XBTUSDM', 'buy', '1')

    # cancel limit order 
    client.cancel_order('5bd6e9286d99522a52e458de')

    # cancel all limit order 
    client.cancel_all_limit_order('XBTUSDM')

    # User
    from kumex.client import User
    client = User(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

    address = client.get_withdrawal_quota('XBT')