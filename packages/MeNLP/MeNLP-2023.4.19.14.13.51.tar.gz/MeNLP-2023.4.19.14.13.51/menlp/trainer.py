#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : trainer
# @Time         : 2023/3/28 16:00
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from functools import partial
import paddle
from paddlenlp.datasets import load_dataset
from paddlenlp.transformers import AutoModelForSequenceClassification, AutoTokenizer
from paddlenlp.trainer import Trainer, TrainingArguments, PdArgumentParser, EarlyStoppingCallback

from paddlenlp.data import DataCollatorWithPadding

from paddle.io import DataLoader, BatchSampler, DistributedBatchSampler

from dataclasses import field

from meutils.pipe import *

pretrained_model_name_or_path = "ernie-3.0-tiny-nano-v2-zh"
num_classes = 2
max_seq_length = 64
model = AutoModelForSequenceClassification.from_pretrained(
    pretrained_model_name_or_path,
    num_classes=num_classes
)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path)


def convert_example(example, tokenizer):
    encoded_inputs = tokenizer(text=example["text"], max_seq_len=8, pad_to_max_seq_len=True)
    encoded_inputs["labels"] = int(example["label"])
    return encoded_inputs


train_ds, dev_ds = load_dataset("chnsenticorp", splits=("train", "dev"))
# train_ds = dev_ds
train_dataset = train_ds.map(partial(convert_example, tokenizer=tokenizer))
eval_dataset = dev_ds.map(partial(convert_example, tokenizer=tokenizer))

args = TrainingArguments('paddle_train',
                         do_train=True, do_eval=True,
                         num_train_epochs=3,
                         per_device_train_batch_size=256,
                         per_device_eval_batch_size=64,
                         evaluation_strategy='steps',
                         load_best_model_at_end=True,
                         logging_steps=10
                         )
trainer = Trainer(
    model=model,
    criterion=paddle.nn.loss.CrossEntropyLoss(),
    args=args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    callbacks=[EarlyStoppingCallback()],

)

trainer.train()
