#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/09 21:20:16 JST.
Last Change: 2019/07/05 22:46:18 JST.

@author: Koki Obinata
"""
import argparse
from distutils.util import strtobool
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--epoch', type=int, default=10,
                        help='number of epochs')
    parser.add_argument('--lr', type=float, default=0.1,
                        help='learning rate')
    parser.add_argument('-f', '--filename', type=str, default='./temp.csv',
                        help='path to the data file')
    parser.add_argument('--check_list', type=list, default=['a', 'b'],
                        help='check file list')
    parser.add_argument('--make_false', action='store_false',
                        help='make some option False (default True)')
    parser.add_argument('--ja', action='store_true',
                        help='enable Japanese (default False)')
    parser.add_argument('--verbose', type=strtobool, default=False,
                        help='convert bool strings to 1(True) or 0(False)')

    args = parser.parse_args()

    OPTION_SAVE_PATH = 'options.json'
    # use json.dump for file writing
    with open(OPTION_SAVE_PATH, mode='w') as f:
        json.dump(obj=vars(args), fp=f,
                  sort_keys=True, indent=2)

    # use json.dumps for print
    print('option: {}'.format(json.dumps(vars(args),
                              sort_keys=True, indent=2)))
