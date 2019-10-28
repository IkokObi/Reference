#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/10/28 14:46:44 JST.
Last Change: 2019/10/28 14:58:22 JST.

参考ページ
https://qiita.com/driller/items/5569871c6cb6bf7d69d4

@author: Koki Obinata
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


fonts = []
for font in fm.findSystemFonts():
    try:
        fonts.append(fm.FontProperties(fname=font).get_name())
    except:
        continue
fonts = set(fonts)
# fonts = set([fm.FontProperties(fname=font).get_name() for font in fm.findSystemFonts()])

fig = plt.figure(figsize=(8, 100))
ax = fig.add_subplot(1, 1, 1)
ax.set_ylim([-0.5, len(fonts)])

for i, f in enumerate(fonts):
    ax.text(0.2, i,  '日本語 {}'.format(f), fontdict={'family': f, 'fontsize': 16})

plt.savefig('output/all_fonts')
