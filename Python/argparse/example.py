#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/09 21:20:16 JST.
Last Change: 2018/11/09 21:44:37 JST.

@author: Koki Obinata
"""
import argparse
import json


A_DEFAULT = 10
B_DEFAULT = 20
C_DEFAULT = 'spam'
D_DEFAULT = ['ham', 'egg']
OPTION_SAVE_PATH = 'options.txt'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--a', type=int, default=A_DEFAULT,
                        help='integer parameter a')
    parser.add_argument('--b', type=float, default=B_DEFAULT,
                        help='float parameter b')
    parser.add_argument('--c', type=str, default=C_DEFAULT,
                        help='string parmeter c')
    parser.add_argument('--d', type=list, default=D_DEFAULT,
                        help='string list d')

    args = parser.parse_args()

    # use json.dump for file writing
    with open(OPTION_SAVE_PATH, mode='w') as f:
        json.dump(obj=vars(args), fp=f,
                  sort_keys=True, indent=2)

    # use json.dumps for print
    print('option: {}'.format(json.dumps(vars(args),
                              sort_keys=True, indent=2)))
