#!/usr/bin/env python
# encoding: utf-8
from urllib import request
import json


class Webhook:
    def __init__(self, url):
        self._url = url
    def _send(self, payload):
        json_data = json.dumps(payload)
        # print('Json data')
        print(json_data)

        req = request.Request(self._url, data=json_data.encode())
        req.add_header('Content-Type', 'application/json')

        res_data = request.urlopen(req)
        res = res_data.read()
        print("Result:")
        print(res)

    def send_card(self, title, message, fields, author_name, author_icon, author_link):
        payload = {
            "attachments": [
                {
                    "type": "Card",
                    "fallback": "Something bad happened",
                    "color": "#00ff2a",
                    "title": title,
                    "text": message,
                    "author_name": author_name,
                    "author_icon": author_icon,
                    "author_link": author_link,
                    "fields": fields
                }
            ]
        }

        self._send(payload)

    def send(self, message):
        self._send({"text": message})
