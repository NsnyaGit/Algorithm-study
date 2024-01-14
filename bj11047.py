#https://www.acmicpc.net/problem/11047

import sys

n,k= map(int,sys.stdin.readline().split())
coin_lst = []
for i in range(n):
    coin_lst.append(int(sys.stdin.readline()))

coin_lst.sort(reverse=True)
cnt = 0
for i in range(n):
    if coin_lst[i] <= k:
        cnt += k//coin_lst[i]
        k %= coin_lst[i]

print(cnt)
