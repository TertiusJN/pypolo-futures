#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests
import hmac
import hashlib
import base64
import time
from uuid import uuid1
from urllib.parse import urljoin

SANDBOX_ENDPOINT = 'https://sandbox-api.kumex.com'
LIVE_ENDPOINT = 'https://api.kumex.com'

# TODO: Change KC to PF

class PoloFuturesBaseRestApi(object):

    def __init__(self, key='', secret='', passphrase='', is_sandbox=False):

        if is_sandbox:
            self.url = SANDBOX_ENDPOINT
        else:
            self.url = LIVE_ENDPOINT
        self.key = key
        self.secret = secret
        self.passphrase = passphrase

    def _request(self, method, uri, timeout=5, auth=True, params=None):
        uri_path = uri
        data_json = ''
        if method in ['GET', 'DELETE']:
            if params:
                strl = []
                for key in sorted(params):
                    strl.append("{}={}".format(key, params[key]))
                data_json += '&'.join(strl)
                uri += '?' + data_json
                uri_path = uri
        else:
            if params:
                data_json= json.dumps(params)

                uri_path = uri + data_json

        headers = {}
        if auth:
            now_time = int(time.time()) * 1000
            str_to_sign = str(now_time) + method + uri_path
            sign = base64.b64encode(
                hmac.new(self.secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
            headers = {
                "KC-API-SIGN": sign,
                "KC-API-TIMESTAMP": str(now_time),
                "KC-API-KEY": self.key,
                "KC-API-PASSPHRASE": self.passphrase,
                "Content-Type": "application/json"
            }
        url = urljoin(self.url, uri)
        if method in ['GET', 'DELETE']:
            response_data = requests.request(method, url, headers=headers, timeout=timeout)
        else:
            response_data = requests.request(method, url, headers=headers, data=data_json,
                                             timeout=timeout)
        return self.check_response_data(response_data)

    @staticmethod
    def check_response_data(response_data):
        if response_data.status_code == 200:
            try:
                data = response_data.json()
            except ValueError:
                raise Exception(response_data.content)
            else:
                if data and data.get('code'):
                    if data.get('code') == '200000':
                        if data.get('data'):
                            return data['data']
                        else:
                            return data
                    else:
                        raise Exception("{}-{}".format(response_data.status_code, response_data.text))
        else:
            raise Exception("{}-{}".format(response_data.status_code, response_data.text))

    @property
    def return_unique_id(self):
        return ''.join([each for each in str(uuid1()).split('-')])
