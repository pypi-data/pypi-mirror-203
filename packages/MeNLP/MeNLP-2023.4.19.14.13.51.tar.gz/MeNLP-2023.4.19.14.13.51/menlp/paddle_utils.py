#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : paddlenlp_utils
# @Time         : 2023/3/22 17:02
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://aistudio.baidu.com/aistudio/projectdetail/5046110
import numpy as np
from meutils.pipe import *

from paddlenlp import Taskflow as _Taskflow
from paddlenlp.transformers import ernie
from paddlenlp.transformers import ErnieForSequenceClassification, ErnieTokenizer

Taskflow = lru_cache()(_Taskflow)

# from paddlenlp.embeddings import TokenEmbedding, list_embedding_name

def get_model(parse='uie'):
    model2url = ernie.configuration.ERNIE_PRETRAINED_RESOURCE_FILES_MAP['model_state']
    return {k: v for k, v in model2url.items() if parse in k}


def taskflow4batch(texts, task_func, batch_size=8):
    return texts | xgroup(batch_size) | xtqdm | xmap_(task_func)


from paddle.io import DataLoader, BatchSampler, DistributedBatchSampler
from paddlenlp.data import DataCollatorWithPadding

def dataloader_from_dataframe(df, batch_size=8, max_seq_length=4, tokenizer=None, shuffle=False):
    def _read(df):
        yield from df.to_dict('r')

    # line = next(_read(df))  # 判断label

    ds = (
        load_dataset(_read, lazy=False, df=df)
            .map(lambda example: {
            **tokenizer(**example, max_seq_len=max_seq_length),
            **{'labels': [example['label']]}
        }) # batch['input_ids'], batch['token_type_ids'], batch['labels']
    )
    batch_sampler = BatchSampler(ds, batch_size=batch_size, shuffle=shuffle)
    collate_fn = DataCollatorWithPadding(tokenizer)
    return DataLoader(dataset=ds, batch_sampler=batch_sampler, collate_fn=collate_fn)




if __name__ == '__main__':
    print(get_model('diffusion'))
