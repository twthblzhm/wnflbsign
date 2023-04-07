# -*- coding: utf8 -*-

"""
cron: 30 5,12,18 * * *
new Env('福利吧签到');
"""

import requests
import re
import os, sys
from sendNotify import send


def start(cookie, username):
    try:
        s = requests.session()
        flb_url = 'www.wnflb2023.com'
        #print(flb_url)
        #print(cookie)
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
                   'cookie': cookie,
                   'dnt': '1',
                   'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                   'sec-ch-ua-mobile': '?0',
                   'sec-ch-ua-platform': "Windows",
                   'sec-fetch-dest': 'document',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-site': 'none',
                   'sec-fetch-user': '?1',
                   'upgrade-insecure-requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'}
        # 访问Pc主页
        user_info = s.get('https://' + flb_url + '/forum-2-1.html', headers=headers,verify=False).text
        #print(user_info)
        #print(username)
        user_name = re.search(r'title="访问我的空间">(.*?)</a>', user_info)
        #print(user_name)
        if user_name:
            print("登录用户名为：" + user_name.group(1))
            print("环境用户名为：" + username)
        else:
            print("未获取到用户名")
        if user_name is None or (user_name.group(1) != username):
            raise Exception("【福利吧】cookie失效???????")
        # 获取签到链接,并签到
        qiandao_url = re.search(r'}function fx_checkin(.*?);', user_info).group(1)
        qiandao_url = qiandao_url[47:-2]
        print(qiandao_url)
        # 签到
        s.get('https://' + flb_url + '/' + qiandao_url, headers=headers).text

        # 获取积分
        user_info = s.get('https://' + flb_url + '/forum.php?mobile=no', headers=headers).text

        current_money = re.search(r'<a.*? id="extcreditmenu".*?>(.*?)</a>', user_info).group(1)
        sing_day = re.search(r'<div class="tip_c">(.*?)</div>', user_info).group(1)
        log_info = "{}当前{}".format(sing_day, current_money)
        print(log_info)
        #send("签到结果", log_info)

    except Exception as e:
        print("签到失败，失败原因:"+str(e))
        #send("签到结果", str(e))


def get_addr():
    pub_page = "http://fuliba2023-1256179406.file.myqcloud.com/"
    ret = requests.get(pub_page)
    ret.encoding = "utf-8"
    bbs_addr = re.findall(r'福利吧论坛地址<a href=.*?><i>https://(.*?)</i></a>', ret.text)[1]
    return bbs_addr


if __name__ == '__main__':
    # cookie = "此处填入COOKIE"
    # username = "此处填入用户名"
    cookie = os.getenv("FUBA")
    user_name = os.getenv("FUBAUN")
    start(cookie, user_name)
