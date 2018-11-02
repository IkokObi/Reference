#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/29 16:46:26 JST.
Last Change: 2018/11/02 11:35:10 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt
import numpy as np


def func(x_arr):
    """
    generate data for plot

    Parameters
    ----------
    x_arr : ndarray

    Return
    ------
    f(x) = 2 * x + 1 + epsilon_noise
    """
    return 2 * x_arr + 1 + np.random.randn(len(x_arr))


def scatter_graph(x_data, y_data, labels, cmap,
                  s=20, marker='o', labelfontsize=14, titlesize=18):
    """ scatter plot """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    n_data = len(x_data)
    for i in range(n_data):
        ax.scatter(x_data[i], y_data[i], s=s, marker=marker, c=cmap(i/n_data))
    # 各点のラベル
    for label, friend_count, minute_count in zip(labels, x_data, y_data):
        ax.annotate(label,
                    xy=(friend_count, minute_count),  # 各点にラベルを付加する
                    xytext=(5, -5),
                    textcoords='offset points')
        # 文字の位置(xytext)を矢印の先からの相対距離(offset points)で指定
    ax.set_xlabel('X Value', fontsize=labelfontsize)
    ax.set_ylabel('Y Value', fontsize=labelfontsize)
    ax.set_title('Scatter Plot with point labels', fontsize=titlesize)
    plt.show()


if __name__ == '__main__':
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    N = 10
    X_DATA = np.arange(N)
    Y_DATA = func(X_DATA)
    LABELS = list(ALPHABET[:N])
    CMAP_NAME = 'gist_rainbow'
    CMAP = plt.get_cmap(CMAP_NAME)

    scatter_graph(x_data=X_DATA, y_data=Y_DATA, labels=LABELS, cmap=CMAP)
