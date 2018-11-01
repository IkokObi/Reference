#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/10/30 14:17:36 JST.
Last Change: 2018/10/30 14:34:22 JST. 

@author: Koki Obinata
"""

import lib.hello as test
from lib.deep_lib.deep_hello import deep_hello 

def call_hello():
    print('Hello from hello.py')
    test.hello()

def call_deep_hello():
    print('Hello from deep_lib.deep_hello.py')
    deep_hello()


if __name__ == '__main__':
    call_hello()
    call_deep_hello()
