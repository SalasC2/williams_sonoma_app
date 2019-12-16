from app import app
from flask import request, jsonify
import urllib, json 
from urllib.request import urlopen, Request

# import requests
import json
import os
import simplejson

@app.route("/retrieveJsonData", methods=["GET"])
def getJsonFile():
    url = "https://www.westelm.com/services/catalog/v4/category/shop/new/all-new/index.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    req = Request(url=url, headers=headers) 
    html = urlopen(req).read() 
    print(html)