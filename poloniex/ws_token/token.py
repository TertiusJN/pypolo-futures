from poloniex.base_request.base_request import PoloFuturesBaseRestApi


class GetToken(PoloFuturesBaseRestApi):

    def get_ws_token(self, is_private=False):
        """
        Public Channels (No authentication is required):
        If you only use public channels (e.g. all public market data), please make request as follows to obtain the server list and temporary public token:
        HTTP Request
        POST /api/v1/bullet-public

        Private Channels (Authentication request required):
        For private channels and messages (e.g. account balance notice), please make request as follows after authorization to obtain the server list and authorized token.
        HTTP Request
        POST /api/v1/bullet-private"""

        uri = '/api/v1/bullet-public'
        if is_private:
            uri = '/api/v1/bullet-private'
        return self._request('POST', uri, auth=is_private)


