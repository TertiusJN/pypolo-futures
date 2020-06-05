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
        elif msg['topic'] == '/contractMarket/level3:XBTUSDM':
            print(f'Get XBTUSDM level3: {msg["data"]}')
        elif msg['topic'] == '/contractMarket/ticker:XBTUSDM':
            print(f'Get XBTUSDM Tick :{msg["data"]}')

    ws = WSToken(API_KEY, SECRET, API_PASS, is_sandbox=SANDBOX)
    ws_client = await PoloFuturesWSClient.create(loop, ws, deal_msg, private=False)

    await ws_client.subscribe('/contractMarket/level2:XBTUSDM')
    await ws_client.subscribe('/contractMarket/level3:XBTUSDM')
    await ws_client.subscribe('/contractMarket/ticker:XBTUSDM')
    while True:
        await asyncio.sleep(0.5, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ws_stream())




