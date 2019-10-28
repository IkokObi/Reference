#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/29 16:46:26 JST.
Last Change: 2018/11/06 21:06:36 JST.

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


def scatter_graph(
    x_data,
    y_data,
    labels,
    cmap,
    s=20,
    marker="o",
    labelfontsize=14,
    titlesize=18,
):
    """ scatter plot """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    n_data = len(x_data)
    for i in range(n_data):  # データ点プロット
        ax.scatter(
            x_data[i], y_data[i], s=s, marker=marker, c=cmap(i / n_data)
        )

    # 各点のラベルをプロット
    for label, friend_count, minute_count in zip(labels, x_data, y_data):
        ax.annotate(
            label,
            xy=(friend_count, minute_count),  # 各点にラベルを付加
            xytext=(5, -5),
            textcoords="offset points",
        )
        # 文字の位置(xytext)を矢印の先からの相対距離(offset points)で指定

    ax.set_xlabel("X Value", fontsize=labelfontsize)  # x軸の設定
    ax.set_ylabel("Y Value", fontsize=labelfontsize)  # y軸の設定

    # タイトル作成
    ax.set_title("Scatter Plot with point labels", fontsize=titlesize)

    plt.show()


if __name__ == "__main__":
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    n_data = 10
    x_data = np.arange(n_data)
    y_data = func(x_data)
    labels = list(ALPHABET[:n_data])
    cmap_name = "gist_rainbow"
    cmap = plt.get_cmap(cmap_name)

    scatter_graph(x_data=x_data, y_data=y_data, labels=labels, cmap=cmap)
