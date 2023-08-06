#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : dataaug
# @Time         : 2023/3/25 20:51
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from paddlenlp.dataaug import WordSubstitute

s1 = "人类语言是抽象的信息符号，其中蕴含着丰富的语义信息，人类可以很轻松地理解其中的含义。"

aug = WordSubstitute('synonym', create_n=1, aug_n=1)
augmented = aug.augment(s1)
print("origin:", s1)
print("augmented:", augmented[0])
