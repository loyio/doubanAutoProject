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

sys.setrecursionlimit(1000000)

emoji_text = ['w(ﾟДﾟ)w', '(ノへ￣、)', '(￣_,￣ )', 'ヽ(✿ﾟ▽ﾟ)ノ', '(๑•̀ㅂ•́)و✧', 'Σ( ° △ °|||)︴',
              '（づ￣3￣）づ╭❤～', '(～￣(OO)￣)ブ', 'φ(≧ω≦*)♪', '(u‿ฺu✿ฺ)', 'Hi~ o(*￣▽￣*)ブ',
              'o(*≧▽≦)ツ┏━┓', '♪(^∇^*)', '╰(*°▽°*)╯', 'o(*^＠^*)o', '(°ー°〃)', 'o(￣ヘ￣o＃)',
              '（＝。＝）', '~~( ﹁ ﹁ ) ~~~', 'o(一︿一+)o', 'o(≧口≦)o', 'ㄟ( ▔, ▔ )ㄏ', '(＠_＠;)']

print()

if __name__ == "__main__":
    while(True):
        # 暖贴专用
        init_no = 0
        topics_url = "https://www.douban.com/group/topic/150598494"
        comment_str = emoji_text[random.randint(0, len(emoji_text)-1)]
        comment_topic_url = topics_url + "/add_comment"
        comment_dict = autocomment.make_comment_dict(comment_topic_url, comment_str, 2)
        print('result', autocomment.comment_topic(comment_topic_url, comment_dict, 2))
        print("成功顶贴一条:", comment_topic_url)
        init_no += 1
        time.sleep(300)
        print("*"*30)