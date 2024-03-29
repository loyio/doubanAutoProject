# -*- coding: utf-8 -*-
"""
Created on 2019/8/27 

@author: LoyeLee
"""
import urllib.request,urllib.parse
import base64
import json

from verifycode import accesstoken
from utils import doubanutils


def get_word_in_pic(pic_path):
    # 给定图片地址 pic_path，识别图片当中的文字

    result = json.loads(accesstoken.get_access_token())
    access_token = result["access_token"]
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(pic_path, 'rb')
    print('pic_path', pic_path)
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode(encoding="utf-8")
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        doubanutils.logger.info("baidu OCR API returns: "+ str(content))
        content = json.loads(content)
        words_result = content["words_result"]
        if len(words_result):
            words = str(words_result[0]["words"]).strip()
            return words.split(" ")[0]
        else:
            return ""
    else:
        return ""