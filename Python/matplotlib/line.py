#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:30:39 JST.
Last Change: 2018/11/06 21:01:16 JST.

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
    f(x) = x^3 + 1 + epsilon_noise
    """
    return x_arr ** 3 + 1 + np.random.randn(len(x_arr))


def line_graph(x_data, y_data, linewidth=2, color="green", marker="o"):
    """ plot line """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(
        x_data,
        y_data,
        color=color,
        marker=marker,
        linewidth=linewidth,
        linestyle="solid",
        label="Line",
    )  # 折れ線グラフ作成

    ax.set_title("Line Plot")  # タイトルを追加
    ax.set_ylabel("Y Value")  # y軸の設定
    plt.legend(loc="upper left")  # 凡例の設定

    plt.show()


if __name__ == "__main__":
    n_data = 10
    x_data = np.arange(n_data)
    y_data = func(x_data)

    line_graph(x_data=x_data, y_data=y_data)
