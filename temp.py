# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=bf7710e0779f4633a4ae35ff778b8f34')

r = requests.get(url)

#print(r.text)
# 返回json，loads处理后，dict变量
data = json.loads(r.text)

articles_num = len(data['articles'])
#print(data['articles'][0]['author'])

# 遍历artles中的所有文章，打印所有的key和value，类似于
# author:
# title:
for article in data['articles']:
    for key in article:
        print(key, ':', article[key])
