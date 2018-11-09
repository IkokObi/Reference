#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2018/11/04 03:50:28 JST.
Last Change: 2018/11/09 19:42:38 JST.

@author: Koki Obinata
"""

from pathlib import Path
import numpy as np


current = Path('.')
data_dir = current / 'Data'
document_a = data_dir / 'a.txt'
document_b = data_dir / 'b.txt'
test_mkdir = current / 'mkdir_test'


""" カレントディレクトリの取得 """
print('Current Path:', current.cwd())


""" ファイル/フォルダの一覧 """
print('\nFiles and Folders')
for path in data_dir.iterdir():
    print('--', path)


""" リストとして取得 """
print('\nGet file list')
list_data = list(data_dir.glob('*.csv'))
print('Data/*.txt', list_data)


""" ファイルの存在チェック """
print('\nFile existance:', document_a, document_a.exists())
print('File existance:', document_b, document_b.exists())


""" ディレクトリの作成/削除 """
print('\nBefore mkdir')
for path in Path('.').iterdir():
    print('--', path)
test_mkdir.mkdir()
print('After mkdir')
for path in Path('.').iterdir():
    print('--', path)
print('\nRemove', test_mkdir)
test_mkdir.rmdir()  # 対象ディレクトリが空でないとエラー
for path in Path('.').iterdir():
    print('--', path)


""" ファイルの読み込み """
print('\nRead', document_a)
with document_a.open('r') as doc_a:
    print(doc_a.readline())

print(document_a.read_text())  # 別の方法での読み込み


""" numpyでも使える """
print('Read', data_dir / 'b.csv')
data_b = np.loadtxt(data_dir / 'b.csv', delimiter=',')
print(data_b)

np.savetxt(data_dir / 'copy_of_b.csv', data_b, fmt='%d', delimiter=':')
