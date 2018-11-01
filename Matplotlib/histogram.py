#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/02 07:58:42 JST.
Last Change: 2018/11/02 08:08:18 JST.

@author: Koki Obinata
"""
from collections import Counter
import matplotlib.pyplot as plt


GRADES = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: (grade // 10) * 10  # //は割り算の商を返す
temp = [decile(grade) for grade in GRADES]
counter_temp = Counter(temp)

def histogram(counter_data):
    """ 1D histogram """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar([x for x in counter_data.keys()],
           counter_data.values(), 8)  # 棒の幅を8にする
    ax.set_xlim([-5, 105])
    ax.set_ylim([0, 5])
    ax.set_xticks([10 * i for i in range(11)])  # x軸のラベル0, 10, ..., 100
    ax.set_xlabel('Declie')
    ax.set_ylabel('# of Students')
    ax.set_title('Distribution of Exam 1 Grades')
    plt.show()


if __name__ == '__main__':
    histogram(counter_data=counter_temp)
