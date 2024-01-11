#N!の結果で、後ろから初めて０じゃない数字が出るまでの０が何個あるかを教えてくれるプログラム作成

import sys

def factorial(n):
    ret = 1
    while n > 0:
        ret *= n
        n-=1
    


n = int(sys.stdin.readline())
