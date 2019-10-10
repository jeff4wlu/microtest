#!/usr/bin/python 
# -*- coding: utf-8 -*-

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/order', methods = ["GET"])
def get_order():
    url = "http://invoice:8000/invoice"
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text + ", 订单一张"
        return text

    return "错误"


@app.route('/', methods = ["GET"])
def health_check():
    return "health_check"
