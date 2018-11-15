#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: yanggd
#date: 2018-04-20
#comment: zabbix接入微信报警脚本

import requests
import sys
import os
import json
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s, %(filename)s, %(levelname)s, %(message)s',
                datefmt = '%a, %d %b %Y %H:%M:%S',
                filename = os.path.join('/usr/local/zabbix/share/zabbix/alertscripts','weixin.log'),
                filemode = 'a')

corpid='ww74f48d9d2c9b62a6'
appsecret='0tn-UrDPgd-ltwOSzFgSzDFIA-B4lcHAPCoM1n5JPUY'
agentid=1000002
#获取accesstoken
token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + appsecret
req=requests.get(token_url)
accesstoken=req.json()['access_token']

#发送消息
msgsend_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken

touser=sys.argv[1]
subject=sys.argv[2]
#toparty='3|4|5|6'
message=sys.argv[3]

params={
        "touser": LiXin,
#       "toparty": 1,
        "msgtype": "text",
        "agentid": 1000002,
        "text": {
                "content": message
        },
        "safe":0
}

req=requests.post(msgsend_url, data=json.dumps(params))

logging.info('sendto:' + touser + ';;subject:' + subject + ';;message:' + message) 

