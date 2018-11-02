#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:50:47 JST.
Last Change: 2018/11/02 10:54:36 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt
import numpy as np

n_category = 5
category = ['Book %d' % i for i in range(1, n_category+1)]
reviews = np.random.randint(low=1, high=11, size=n_category)


def bar_graph(data, labels):
    """ 棒グラフ """
    xticks = [i for i, _ in enumerate(labels)]  # 棒グラフのx軸を作成

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(xticks, data)  # 棒グラフを作る
    ax.set_ylabel('Review (10 rank)')
    ax.set_ylim([0, 10.5])
    ax.set_title('Book Reviews')
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    # x軸のラベルに映画名を配置
    plt.show()


if __name__ == '__main__':
    bar_graph(data=reviews, labels=category)
