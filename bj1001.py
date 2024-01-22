#整数A,Bの値が与えられた時、A-Bを出力するプログラムを作成

import sys

A, B = map(int, sys.stdin.readline().rstrip('/n').split())

print(A-B)
