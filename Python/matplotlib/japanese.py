#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/10/28 13:57:04 JST.
Last Change: 2019/10/28 14:58:07 JST.

参考ページ
https://qiita.com/yniji/items/3fac25c2ffa316990d0c

@author: Koki Obinata
"""
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams["font.family"] = "sans-serif"
font_list = [
    "Hiragino Mincho ProN",
    "Hiragino Maru Gothic Pro",
    "YuGothic",
    "Noto Sans Mono CJK JP",
    "IPAPGothic",
]
rcParams["font.sans-serif"] = font_list

x = np.arange(11) - 5
y = x ** 2

for i in range(len(font_list)):
    rcParams["font.sans-serif"] = font_list[i:]
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="日本語の設定")
    ax.set_title("日本語のタイトル設定(Title)")
    ax.legend(loc="upper right")
    plt.savefig("output/{}".format(font_list[i]), dpi=200)
