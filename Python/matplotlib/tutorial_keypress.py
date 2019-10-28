#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/12/11 13:32:41 JST.
Last Change: 2018/12/11 13:32:49 JST.

@author: Koki Obinata
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def press(event):
    print("press", event.key)
    sys.stdout.flush()
    if event.key == "x":
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()


# Fixing random state for reproducibility
np.random.seed(19680801)


fig, ax = plt.subplots()

fig.canvas.mpl_connect("key_press_event", press)

ax.plot(np.random.rand(12), np.random.rand(12), "go")
xl = ax.set_xlabel("easy come, easy go")
ax.set_title("Press a key")
plt.show()
