#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/09 21:20:16 JST.
Last Change: 2019/10/03 18:18:16 JST.

@author: Koki Obinata
"""
import argparse
from distutils.util import strtobool
import json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--name", type=str, help="some name")
    parser.add_argument("--epoch", type=int, default=10, help="number of epochs")
    parser.add_argument("--lr", type=float, default=0.1, help="learning rate")
    parser.add_argument(
        "-f", "--filepath", type=str, default="./temp.csv", help="path to the data file"
    )
    parser.add_argument(
        "--check-list", type=list, default=["a", "b"], help="check file list"
    )
    parser.add_argument(
        "--make-false",
        action="store_false",
        help="make some option False (default True)",
    )
    parser.add_argument(
        "--ja", action="store_true", help="enable Japanese (default False)"
    )
    parser.add_argument(
        "--verbose",
        type=strtobool,
        default=False,
        help="convert bool strings to 1(True) or 0(False)",
    )
    parser.add_argument(
        "--choice",
        default="spam",
        choices=["spam", "ham", "egg"],
        help="convert bool strings to 1(True) or 0(False)",
    )

    args = parser.parse_args()
    print(args)

    OPTION_SAVE_PATH = "options.json"
    # use json.dump for file writing
    with open(OPTION_SAVE_PATH, mode="w") as f:
        json.dump(obj=vars(args), fp=f, sort_keys=True, indent=2)

    # use json.dumps for print
    print("option: {}".format(json.dumps(vars(args), sort_keys=True, indent=2)))
