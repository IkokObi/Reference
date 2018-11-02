#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:30:39 JST.
Last Change: 2018/11/02 10:00:08 JST.

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


DATANUM = 10
X_DATA = np.arange(DATANUM)
Y_DATA = func(X_DATA)


def line_graph(x, y):
    """ plot line """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='green', marker='o', linestyle='solid')
    ax.set_title('Line Plot')  # タイトルを追加
    ax.set_ylabel('Y Value')  # y軸にラベルを追加
    plt.show()


if __name__ == '__main__':
    line_graph(x=X_DATA, y=Y_DATA)
