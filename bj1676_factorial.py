#N!の結果で、後ろから初めて０じゃない数字が出るまでの０が何個あるかを教えてくれるプログラム作成

def factorial(n):
    ret = 1
    while n > 0:
        ret *= n
        n-=1
    return ret

import sys

cnt = 0
n = int(sys.stdin.readline())
n = str(factorial(n))

for i in range(1, len(n)+1):
    if n[-i] != '0':
        break
    else:
        cnt+=1
        
print(cnt)

# 다른 답
# n = int(sys.stdin.readline())
# print(n//5 + n//25 + n//125)