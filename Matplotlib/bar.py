#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:50:47 JST.
Last Change: 2018/11/02 08:09:59 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt

MOVIES = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
NUM_OSCARS = [5, 11, 3, 8, 10]


def bar_graph(data, labels):
    """ 棒グラフ """
    xticks = [i for i, _ in enumerate(labels)]  # 棒グラフのx軸を作成

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(xticks, data)  # 棒グラフを作る
    ax.set_ylabel('# of Academy Awards')
    ax.set_title('My Favorite Movies')
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    # x軸のラベルに映画名を配置
    plt.show()


if __name__ == '__main__':
    bar_graph(data=NUM_OSCARS, labels=MOVIES)
