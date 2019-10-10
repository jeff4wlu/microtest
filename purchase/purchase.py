#!/usr/bin/python 
# -*- coding: utf-8 -*-

from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/purchase', methods = ["GET"])
def get_purchase():

    url = "http://order:8000/order"
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text + ", 成功购买！"
        return text

    return "错误"

@app.route('/', methods = ["GET"])
def health_check():
    return "health check"

