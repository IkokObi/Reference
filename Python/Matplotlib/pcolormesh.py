#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/04 04:46:18 JST.
Last Change: 2018/11/04 05:17:16 JST.

@author: Koki Obinata
"""

import matplotlib.pyplot as plt
import numpy as np


def pcolormesh(x_grid, y_grid, data):
    """ plot 2D histogram """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    quadmesh = ax.pcolormesh(x_grid, y_grid, data)
    cbar = fig.colorbar(quadmesh, ax=ax)
    cbar.set_label('Color Bar')
    print(cbar)
    plt.show()


if __name__ == '__main__':
    # 第1要素がY軸, 第2要素がX軸となることに注意
    X, Y = np.meshgrid(np.linspace(0, 2, 200), np.linspace(0, 3, 300))
    print('X shape:', X.shape)
    print('Y shape:', Y.shape)

    DATA = np.sin(2*np.pi*X) * (Y+1) * (3-Y)
    pcolormesh(x_grid=X, y_grid=Y, data=DATA)
