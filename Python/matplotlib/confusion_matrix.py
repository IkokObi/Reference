#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/29 14:30:09 JST.
Last Change: 2018/12/22 16:51:41 JST.

@author: Koki Obinata
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix


def print_cmx(y_true, y_pred, labels, name_labels, name):
    """ 混同行列のプロット """
    # 混同行列を作成, c_ij は真のグループが i で予測グループが j の数を表す
    cmx_data = confusion_matrix(y_true, y_pred, labels=labels)

    # プロット用のpd.DataFrame型
    df_cmx = pd.DataFrame(cmx_data, index=name_labels, columns=name_labels)

    plt.figure(figsize=(8, 6))
    sn.heatmap(df_cmx, annot=True, fmt='d', cmap='Blues')
    plt.show()
    # plt.savefig(name)


if __name__ == '__main__':
    y_true = np.array([1, 1, 2, 3, 1, 1, 2, 2, 3, 2, 1])
    y_pred = np.array([1, 2, 2, 3, 2, 1, 2, 3, 3, 2, 3])
    labels = [1, 2, 3]
    name_labels = ['spam', 'ham', 'egg']
    # name_labels = labels
    name = 'confusion_matrix'
    print_cmx(y_true, y_pred, labels, name_labels, name)
