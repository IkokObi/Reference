#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/29 16:46:26 JST.
Last Change: 2018/11/02 10:00:28 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt
import numpy as np


def func(x):
    """
    generate data for plot 

    Parameters
    ----------
    x : ndarray

    Return
    ------
    f(x) = 2 * x + 1 + epsilon_noise
    """
    return 2 * x + 1 + np.random.randn(len(x))


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
DATANUM = 10
X_DATA = np.arange(DATANUM)
Y_DATA = func(X_DATA)
LABELS = list(ALPHABET[:DATANUM])


def scatter_graph(x, y, labels):
    """ scatter plot """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    # 各点のラベル
    for label, friend_count, minute_count in zip(labels, x, y):
        ax.annotate(label,
                    xy=(friend_count, minute_count),  # 各点にラベルを付加する
                    xytext=(5, -5),
                    textcoords='offset points')
        # 文字の位置(xytext)を矢印の先からの相対距離(offset points)で指定
    ax.set_xlabel('X Value')
    ax.set_ylabel('Y Value')
    ax.set_title('Scatter Plot with point labels')
    plt.show()


if __name__ == '__main__':
    scatter_graph(x=X_DATA, y=y_data, labels=LABELS)
