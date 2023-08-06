#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ie_utils
# @Time         : 2023/4/7 17:45
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
import jmespath

data = [
    {'人物': [
        {'text': '王教头',
         'start': 7,
         'end': 10,
         'probability': 0.5978589893137567,
         'relations': {'父亲': [{'text': '王员外', 'start': 270, 'end': 273, 'probability': 0.6976410636509378}]}},

        {'text': 'xx'}
    ]},
    {'人物': [
        {'text': 'xx'}
    ]}
]
r = jmespath.search(
    '[*].*[*].[text, relations | [keys(not_null(@))][]| @[0] , relations.*[].text | @[0]][][] | [?not_null(@[-1])]',
    data)
print(r)  # 三元组

data = [{'评价维度': [{'text': '江水',
    'start': 34,
    'end': 36,
    'probability': 0.4445239599660056,
    'relations': {'观点词': [{'text': '清清',
       'start': 31,
       'end': 33,
       'probability': 0.9846463741426135}, {'text': '清清清清清清清清',
       'start': 31,
       'end': 33,
       'probability': 0.9846463741426135}],
     '情感倾向[正向,负向]': [{'text': '正向', 'probability': 0.9998170214937545}]}}]},
 {},
 {'评价维度': [{'text': '文化',
    'start': 27,
    'end': 29,
    'probability': 0.4537145943045715,
    'relations': {'观点词': [{'text': '独特',
       'start': 35,
       'end': 37,
       'probability': 0.9348730647808026}],
     '情感倾向[正向,负向]': [{'text': '正向', 'probability': 0.9995695180754538}]}}]},
 {},
 {'评价维度': [{'text': '特色',
    'start': 50,
    'end': 52,
    'probability': 0.8780129641562233,
    'relations': {'观点词': [{'text': '鲜明',
       'start': 52,
       'end': 54,
       'probability': 0.9995288131254654}],
     '情感倾向[正向,负向]': [{'text': '正向', 'probability': 0.9996272672880657}]}}]}]

jmespath.search(
    '[*].*[*].[text, relations | [keys(not_null(@))][]| @[0] , relations.*[*].text | @[0]][][] | [?not_null(@[-1])]',
    data)
data = [{'日期': [{'text': '2021年8月4日',
                   'start': 134,
                   'end': 143,
                   'probability': 0.47987788825388833}],
         '姓名': [{'text': '张某某',
                   'start': 4,
                   'end': 7,
                   'probability': 0.664319935259222}]}]

keys = jmespath.search('[*] | keys(@[0]) ', data)  # 日期 姓名
values = jmespath.search('[*].*[*].text[] ', data)
