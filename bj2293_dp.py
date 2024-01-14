#n個の種類を持つコインがある。各コインが表す価値は互いに異なっている。
#このコインを使って、価値の合がkウォンになるようにしたい時これは何通りあるかを教えてくれるプログラムを作成
#ただし各コインは何個でも使用可能であり、使用したコインの構成が一緒の時、その順序が違っても同じ通りとみなす。

import sys

n,k= map(int,sys.stdin.readline().split())
coin_lst = []
for i in range(n):
    coin_lst.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
dp[0] = 1
for i in coin_lst:
    for j in range(i,k+1):
        dp[j] = dp[j] + dp[j-i]

print(dp[k])

