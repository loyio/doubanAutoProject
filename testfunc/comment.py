# -*- coding: utf-8 -*-
"""
Created on 2019/8/27 

@author: LoyeLee
"""
import time
import sys
import random

sys.path.append('/Users/susmote/PycharmProjects/doubanAutoProject')
from group import autocomment
from utils import doubanutils

sys.setrecursionlimit(1000000)

emoji_text = ['w(ﾟДﾟ)w', '(ノへ￣、)', '(￣_,￣ )', 'ヽ(✿ﾟ▽ﾟ)ノ', '(๑•̀ㅂ•́)و✧', 'Σ( ° △ °|||)︴',
              '（づ￣3￣）づ╭❤～', '(～￣(OO)￣)ブ', 'φ(≧ω≦*)♪', '(u‿ฺu✿ฺ)', 'Hi~ o(*￣▽￣*)ブ',
              'o(*≧▽≦)ツ┏━┓', '♪(^∇^*)', '╰(*°▽°*)╯', 'o(*^＠^*)o', '(°ー°〃)', 'o(￣ヘ￣o＃)',
              '（＝。＝）', '~~( ﹁ ﹁ ) ~~~', 'o(一︿一+)o', 'o(≧口≦)o', 'ㄟ( ▔, ▔ )ㄏ', '(＠_＠;)']

print()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("请在运行文件后面加上你要顶帖的链接")
        exit(0)
    while(True):
        # 暖贴专用
        init_no = 0
        topics_url = sys.argv[1]
        comment_str = emoji_text[random.randint(0, len(emoji_text)-1)]
        comment_topic_url = topics_url + "/add_comment"
        pic_url, pic_id = "", ""
        comment_dict = autocomment.make_comment_dict(comment_topic_url, comment_str, 3, pic_url, pic_id)
        res = autocomment.comment_topic(comment_topic_url, comment_dict, 3)
        while(True):
            pic_url, pic_id = doubanutils.get_image_and_id(res)
            if pic_url == "" or pic_id == "":
                print("顶帖成功:", comment_str)
                break
            else:
                print("正在解析验证码!!!")
                comment_dict = autocomment.make_comment_dict(comment_topic_url, comment_str, 3, pic_url, pic_id)
                res = autocomment.comment_topic(comment_topic_url, comment_dict, 3)
        init_no += 1
        print("*"*30)
        time.sleep(360)
