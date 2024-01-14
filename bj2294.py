#https://www.acmicpc.net/problem/2294

import sys

n,k= map(int,sys.stdin.readline().split())
coin_lst = []
for i in range(n):
    coin_lst.append(int(sys.stdin.readline()))

dp = [0]+[-1] * k

for i in range(1, k+1):
    lst = []
    for j in coin_lst:
        if i-j >= 0 and dp[i-j] != -1:
            lst.append(dp[i-j])
    if len(lst) != 0:
        dp[i] = min(lst) + 1

print(dp[k])