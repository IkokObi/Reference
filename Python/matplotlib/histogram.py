#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:58:42 JST.
Last Change: 2018/11/24 20:36:41 JST.

@author: Koki Obinata
"""
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def histogram(counter_data):
    """ 1D histogram """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.bar([x for x in counter_data.keys()],
           counter_data.values(), 8)  # ヒストグラム作成, 棒の幅を8にする
    ax.set_xlim([-5, 105])  # x軸の設定
    ax.set_xlabel('Declie')
    ax.set_xticks([10 * i for i in range(11)])  # x軸のラベル0, 10, ..., 100

    ax.set_ylim([0, 10])  # y軸の設定
    ax.set_ylabel('# of Students')

    ax.set_title('Score Distribution of Exam 1')  # タイトルの追加

    plt.show()


def decile(data):
    """
    十分位変換

    Parameters
    ----------
    data : ndarray, shape = [n_data]
    """
    return (data // 10) * 10


if __name__ == '__main__':
    n_students = 20
    grades = np.random.randint(low=0, high=101, size=n_students)
    grades_counter = Counter(decile(grades))

    histogram(counter_data=grades_counter)
