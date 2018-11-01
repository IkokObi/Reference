#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/29 16:46:26 JST.
Last Change: 2018/11/02 08:09:15 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt


FRIENDS = [70, 65, 72, 63, 71, 64, 60, 64, 67]
MINUTES = [175, 170, 205, 120, 220, 130, 105, 145, 190]
LABELS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def scatter_graph(x, y, labels):
    """ scatter plot """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    # 各点のラベル
    for label, friend_count, minute_count in zip(labels, x, y):
        ax.annotate(label,
                    xy=(friend_count, minute_count),  # 各点にラベルを付加する
                    xytext=(5, -5),
                    textcoords='offset points')
        # 文字の位置(xytext)を矢印の先からの相対距離(offset points)で指定
    ax.set_xlabel('# of friends')
    ax.set_ylabel('daily minutes spent on the site')
    ax.set_title('Daily Minutes vs. Number of Friends')
    plt.show()


if __name__ == '__main__':
    scatter_graph(x=FRIENDS, y=MINUTES, labels=LABELS)
