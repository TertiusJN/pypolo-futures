#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='pypolo-futures',
    version='v0.1.0',
    packages=['poloniex', 'poloniex/base_request', 'poloniex/market_data', 'poloniex/trade', 'poloniex/user',
              'poloniex/websocket', 'poloniex/ws_token'],
    license="MIT",
    author='Tertius Nel',
    author_email="tnel@poloniex.com",
    url='https://github.com/Poloniex/pypolo-futures',
    description="Poloniex Futures Exchange Python 3 Wrapper",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
