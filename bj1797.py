#互いに違うN個の自然数の合をSとする。Sを知ってる時に、自然数Nの最大値を求めよ

import sys

s = int(sys.stdin.readline())
cnt = 0
v = 0
i = 1
while True:
    v += i
    if s >= v:
        cnt+=1
    else:
        break
    i+=1
print(cnt)