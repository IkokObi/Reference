#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/29 16:46:26 JST.
Last Change: 2018/11/02 10:51:31 JST.

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
n_data = 10
x_data = np.arange(n_data)
y_data = func(x_data)
labels = list(ALPHABET[:n_data])
cmap_name = 'gist_rainbow'
cmap = plt.get_cmap(cmap_name)


def scatter_graph(x, y, labels, cmap, s=20, marker='o', c='orange',
                  labelfontsize=14, titlesize=18):
    """ scatter plot """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(len(x)):
        ax.scatter(x[i], y[i], s=s, marker=marker, c=cmap(i/len(x)))
    # 各点のラベル
    for label, friend_count, minute_count in zip(labels, x, y):
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
    scatter_graph(x=x_data, y=y_data, labels=labels, cmap=cmap)
