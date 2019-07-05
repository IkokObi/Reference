#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/07 14:21:04 JST.
Last Change: 2019/07/05 22:52:10 JST.


時間計測を簡単に行うことが出来る
Reference
- https://qiita.com/tag1216/items/e1e3c565a2bf8dbc7f86
エラーの例外処理
- https://blog.amedama.jp/entry/2015/10/02/234946

@author: Koki Obinata
"""
import time
from contextlib import contextmanager
from collections import defaultdict


@contextmanager
def single_timer(label):
    """
    処理の時間を計測

    Usage
    -----
    with single_timer('some_process'):
        time.sleep(0.1)

    Parameters
    ----------
    label : str
        計測した処理時間を表示する際の名前
    """
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {:.4f}'.format(label, end-start))


@contextmanager
def timer_for_each():
    """
    forループの中などで，処理ごとに別々に時間を計測

    Usage
    -----
    with timer_for_each() as timer:
        for _ in range(10):
            with timer('process1'):
                time.sleep(0.1)

            with timer('process2'):
                time.sleep(0.2)

    Parameters
    ----------
    label : str
        計測した処理時間を表示する際の名前
    """
    times = defaultdict(float)

    @contextmanager
    def timer(label):
        start = time.time()
        try:
            yield
        finally:
            end = time.time()
            times[label] += end - start

    yield timer

    for label, t in times.items():
        print('{}: {:.4f}'.format(label, t))


@contextmanager
def timer_for_total(total_label):
    """
    forループの中などで，処理ごとに別々に時間を計測し，
    最後に全体の処理時間を表示

    Usage
    -----
    with timer_for_total('Total time') as timer:
        for _ in range(10):

            with timer('process1'):
                time.sleep(0.1)

            with timer('process2'):
                time.sleep(0.2)

    Parameters
    ----------
    total_label : str
        全体の処理時間を表示する際の名前

    label : str
        計測した処理時間を表示する際の名前
    """
    times = defaultdict(float)

    @contextmanager
    def timer(label):
        start = time.time()
        try:
            yield
        finally:
            end = time.time()
            times[label] += end - start

    with timer(total_label):
        yield timer

    for label, t in times.items():
        if label != total_label:
            print('{}: {:.3f}'.format(label, t))
    print('{}: {:.3f}'.format(total_label, times[total_label]))


if __name__ == '__main__':
    # 1種類の処理時間
    with single_timer('for loop'):
        MOD = 10**9 + 7
        a = 0
        for i in range(10**6):
            a += i
            a %= MOD

    # 各処理の処理時間
    with timer_for_each() as timer:
        for _ in range(10):
            with timer('処理1'):
                time.sleep(0.1)

            with timer('処理2'):
                time.sleep(0.2)

    # 各処理 + 全体の処理時間
    with timer_for_total('全体') as timer:
        for _ in range(10):
            with timer('処理1'):
                time.sleep(0.1)

            with timer('処理2'):
                time.sleep(0.2)

    # 例外時の処理
    with single_timer('Error handling'):
        print("Let's raise error")
        raise Exception('Error occured!')
