#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='python-poloniex',
    version='v1.1.0',
    packages=['poloniex', 'poloniex/base_request', 'poloniex/market_data', 'poloniex/trade', 'poloniex/user',
              'poloniex/websocket', 'poloniex/ws_token'],
    license="MIT",
    author='Grape',
    author_email="grape.zhang@kucoin.com",
    url='https://github.com/Kucoin/kumex-python-sdk',
    description="poloniex-api-sdk",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
