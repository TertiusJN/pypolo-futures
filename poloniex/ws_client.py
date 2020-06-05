from poloniex.websocket.websocket import ConnectWebsocket

class PoloFuturesWSClient:
    """
    https://docs.kumex.com/#websocket-2
    """

    def __init__(self):
        self._callback = None
        self._conn = None
        self._loop = None
        self._client = None
        self._private = False

    @classmethod
    async def create(cls, loop, client, callback, private=False):
        self = PoloFuturesWSClient()
        self._loop = loop
        self._client = client
        self._private = private
        self._callback = callback
        self._conn = ConnectWebsocket(loop, self._client, self._recv, private)
        return self

    async def _recv(self, msg):
        if 'data' in msg:
            await self._callback(msg)

    async def subscribe(self, topic):
        """
        To subscribe channel messages from a certain server, the client side should send subscription message to the server.
        If the subscription succeeds, the system will send ack messages to you, when the response is set as true.
        While there are topic messages generated, the system will send the corresponding messages to the client side.
        For details about the message format, please check the definitions of topics."""

        req_msg = {'type': 'subscribe', 'topic': topic, 'response': True}
        await self._conn.send_message(req_msg)

    async def unsubscribe(self, topic):
        """
        Unsubscribe from topics you have subscribed to."""

        req_msg = {'type': 'unsubscribe', 'topic': topic, 'response': True}
        await self._conn.send_message(req_msg)
