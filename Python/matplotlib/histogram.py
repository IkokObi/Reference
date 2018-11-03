#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:58:42 JST.
Last Change: 2018/11/02 11:18:50 JST.

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
           counter_data.values(), 8)  # 棒の幅を8にする
    ax.set_xlim([-5, 105])
    ax.set_ylim([0, 10])
    ax.set_xticks([10 * i for i in range(11)])  # x軸のラベル0, 10, ..., 100
    ax.set_xlabel('Declie')
    ax.set_ylabel('# of Students')
    ax.set_title('Score Distribution of Exam 1')
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
    N_STUDENTS = 20
    GRADES = np.random.randint(low=0, high=101, size=N_STUDENTS)
    GRADES_COUNTER = Counter(decile(GRADES))

    histogram(counter_data=GRADES_COUNTER)
