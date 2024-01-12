#n個の種類を持つコインがある。各コインが表す価値は互いに異なっている。
#このコインを使って、価値の合がkウォンになるようにしたい時これは何通りあるかを教えてくれるプログラムを作成
#ただし各コインは何個でも使用可能であり、使用したコインの構成が一緒の時、その順序が違っても同じ通りとみなす。

import sys


n,k= map(int,sys.stdin.readline().split())

value_of_coin = []
for i in range(n):
    value_of_coin.append(int(sys.stdin.readline()))

value_of_coin.sort()