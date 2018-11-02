#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:30:39 JST.
Last Change: 2018/11/02 10:52:38 JST.

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
    f(x) = x^3 + 1 + epsilon_noise
    """
    return x ** 3 + 1 + np.random.randn(len(x))


n_data = 10
x_data = np.arange(n_data)
y_data = func(x_data)


def line_graph(x, y, linewidth=2, c='green', marker='o'):
    """ plot line """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color=c, marker=marker, linewidth=linewidth, linestyle='solid')
    ax.set_title('Line Plot')  # タイトルを追加
    ax.set_ylabel('Y Value')  # y軸にラベルを追加
    plt.show()


if __name__ == '__main__':
    line_graph(x=x_data, y=y_data)
