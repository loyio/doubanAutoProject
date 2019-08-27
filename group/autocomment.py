# -*- coding: utf-8 -*-
"""
Created on 2019/8/27 

@author: LoyeLee
"""
import requests

from utils import doubanutils,tools
from verifycode import wordrecognition
from PIL import Image
from utils.convert import reduce_noisy, gen_white_black_points


def comment_topic(topic_url, comment_dict, cookie_no):
    # 在一个帖子下发表回复

    r = requests.post(topic_url, cookies=doubanutils.get_cookies(cookie_no),
                      data=comment_dict)
    doubanutils.logger.info("in func comment_topic(), " +
                           str(comment_dict) + ", status_code: " + str(r.status_code))
    return r.text


def make_comment_dict(topic_url, rv_comment, cookie_no):
    # 组装回帖的参数

    pic_url, pic_id = doubanutils.get_verify_code_pic(topic_url, cookie_no)
    verify_code = ""
    if len(pic_url):
        pic_path = tools.save_pic_to_disk(pic_url)
        img = Image.open(pic_path)
        img = img.convert('RGBA')
        w, h = img.size[0], img.size[1]
        point_list = gen_white_black_points(img)
        reduce_noisy(w, h, point_list)
        img.putdata(point_list)
        img.save("rebuild.png")
        verify_code = wordrecognition.get_word_in_pic("rebuild.png")
        verify_code = verify_code.lower()
    comment_dict = {
        "ck": doubanutils.get_form_ck_from_cookie(cookie_no),
        "rv_comment": rv_comment,
        "start": 0,
        "img":"",
        "captcha-solution": verify_code,
        "captcha-id": pic_id,
        "submit_btn": "发送"
    }
    return comment_dict
