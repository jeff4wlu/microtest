#!/usr/bin/python 
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/invoice', methods = ['GET'])
def get_invoice():

    return "发票一张"

@app.route('/', methods = ['GET'])
def health_check():
    return "health check"
