#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/04 04:46:18 JST.
Last Change: 2018/11/06 21:09:35 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt
import numpy as np


EPSILON = 10 ** (-8)


def pcolormesh(x_grid, y_grid, data, vmin, vmax, tickstep=0.5):
    """ plot 2D histogram """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    quadmesh = ax.pcolormesh(
        x_grid, y_grid, data, vmin=vmin, vmax=vmax
    )  # ヒートマップ作成

    cbar = fig.colorbar(quadmesh, ax=ax)  # カラーバー作成
    cbar.set_label("Color Bar")

    # x軸の設定
    xticks = np.arange(
        x_grid[0, 0], x_grid[0, -1] // tickstep * tickstep + EPSILON, tickstep
    )
    ax.set_xticks(xticks)

    # y軸の設定
    yticks = np.arange(
        y_grid[0, 0], y_grid[-1, 0] // tickstep * tickstep + EPSILON, tickstep
    )
    ax.set_yticks(yticks)

    # カラーバーの設定
    cticks = np.arange(vmin, vmax + EPSILON, tickstep)
    cbar.set_ticks(cticks)

    plt.show()


if __name__ == "__main__":
    # 第1要素がY軸, 第2要素がX軸となることに注意
    X, Y = np.meshgrid(np.linspace(0, 2, 200), np.linspace(0, 3, 300))
    print("X shape:", X.shape)
    print("Y shape:", Y.shape)

    data = np.sin(2 * np.pi * X) * (Y + 1) * (3 - Y)
    pcolormesh(x_grid=X, y_grid=Y, data=data, vmin=-4, vmax=4)
