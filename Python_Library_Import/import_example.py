#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/30 14:16:12 JST.
Last Change: 2018/11/03 23:30:52 JST.

Description:
    pythonのライブラリimport関係の確認

@author: Koki Obinata
"""

import lib.caller as caller


if __name__ == '__main__':
    caller.call_hello()
    caller.call_deep_hello()

