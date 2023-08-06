#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : metrics
# @Time         : 2023/4/4 18:50
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

import torch
from torchmetrics.functional import (
    auroc,
    accuracy,
    confusion_matrix,
    precision, recall, f1_score, specificity,
    average_precision
)

import torchmetrics

from sklearn.metrics import precision_recall_curve, average_precision_score, roc_curve, auc, precision_score, \
    recall_score, f1_score, confusion_matrix, accuracy_score


def compute_metrics(eval_pred, task='multiclass', num_classes=16):  # ["binary", "multiclass", "multilabel"]
    #     global x
    #     x = eval_pred
    num_labels = None

    logits, labels = eval_pred
    preds = torch.FloatTensor(logits)  # todo 是否需要转换
    target = torch.IntTensor(labels)

    metrics = {}
    metrics['auc'] = auroc(preds, target, task, num_classes=num_classes)
    metrics['acc'] = accuracy(preds, target, task, num_classes=num_classes)
    metrics['f1'] = f1_score(preds, target, task, num_classes=num_classes)

    # ap = average_precision(preds, target, task=task, num_classes=num_classes)

    return metrics
