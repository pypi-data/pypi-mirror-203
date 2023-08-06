#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : multiclass
# @Time         : 2023/4/4 18:48
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *

import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split

from transformers import AutoModel, AutoTokenizer, AdamW, AutoModelForSequenceClassification
from transformers import get_linear_schedule_with_warmup

from torchmetrics.functional import accuracy, auroc, average_precision, precision
import torchmetrics
import datasets

# ME
from meutils.pipe import *

# 常量
RANDOM_SEED = 42
MAX_EPOCHS = 1
BATCH_SIZE = 128
MAX_LENGTH = 128
PRE_TRAINED_MODEL_NAME = 'ckiplab/albert-tiny-chinese'
tokenizer = AutoTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
