#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:30:39 JST.
Last Change: 2018/11/02 08:08:40 JST.

@author: Koki Obinata
"""
import matplotlib.pyplot as plt


YEARS = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
GDP = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]


def line_graph(x, y):
    """ plot line """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='green', marker='o', linestyle='solid')
    ax.set_title('Nominal GDP')  # タイトルを追加
    ax.set_ylabel('Billion of $')  # y軸にラベルを追加
    plt.show()


if __name__ == '__main__':
    line_graph(x=YEARS, y=GDP)
