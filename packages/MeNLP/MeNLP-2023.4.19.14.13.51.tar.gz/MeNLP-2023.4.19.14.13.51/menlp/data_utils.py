#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : data_utils
# @Time         : 2023/3/25 21:35
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from paddle.io import DataLoader, BatchSampler, DistributedBatchSampler
from paddlenlp.data import DataCollatorWithPadding
from paddlenlp.datasets import load_dataset

from paddlenlp.trainer import Trainer, TrainingArguments, PdArgumentParser

def dataloader_from_dataframe(df, batch_size=8, max_seq_length=4, tokenizer=None, shuffle=False):
    assert 'label' in df
    assert tokenizer

    def read_func():
        yield from df.to_dict('r')

    # line = next(_read(df))  # 判断label

    ds = (
        load_dataset(read_func, lazy=False)
        .map(lambda example: {
            **tokenizer(**example, max_seq_len=max_seq_length),
            **{'labels': [example['label']]}
        })  # batch['input_ids'], batch['token_type_ids'], batch['labels']
    )
    batch_sampler = BatchSampler(ds, batch_size=batch_size, shuffle=shuffle)
    collate_fn = DataCollatorWithPadding(tokenizer)
    return DataLoader(dataset=ds, batch_sampler=batch_sampler, collate_fn=collate_fn)


def dataloader(dict_iter, batch_size=8, max_seq_length=4, tokenizer=None, shuffle=False):
    assert tokenizer
    ds = (
        load_dataset(lambda: dict_iter, lazy=False)
        .map(lambda example: {
            **tokenizer(**example, max_seq_len=max_seq_length),
            **{'labels': [example['label']]}
        })  # batch['input_ids'], batch['token_type_ids'], batch['labels']
    )
    batch_sampler = BatchSampler(ds, batch_size=batch_size, shuffle=shuffle)
    collate_fn = DataCollatorWithPadding(tokenizer)

    return DataLoader(dataset=ds, batch_sampler=batch_sampler, collate_fn=collate_fn)


def dataloader_from_dataframe(df, batch_size=8, max_seq_length=4, tokenizer=None, shuffle=False):
    assert 'label' in df

    return dataloader(df.to_dict('r'), batch_size, max_seq_length, tokenizer, shuffle)
