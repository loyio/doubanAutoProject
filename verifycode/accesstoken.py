# -*- coding: utf-8 -*-
"""
Created on 2019/8/27 

@author: LoyeLee
"""
import urllib.request
from config import bdrecog as config


def get_access_token():
    # 获取百度AI开放平台的access_token
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+config.API_KEY+'&client_secret='+config.SECRET_KEY
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        return content