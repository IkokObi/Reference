#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:30:39 JST.
Last Change: 2018/11/02 12:40:50 JST.

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


def line_graph(x_data, y_data, linewidth=2, color='green', marker='o'):
    """ plot line """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_data, y_data, color=color, marker=marker, linewidth=linewidth,
            linestyle='solid', label='Line')
    ax.set_title('Line Plot')  # タイトルを追加
    ax.set_ylabel('Y Value')  # y軸にラベルを追加
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    N = 10
    X_DATA = np.arange(N)
    Y_DATA = func(X_DATA)

    line_graph(x_data=X_DATA, y_data=Y_DATA)
