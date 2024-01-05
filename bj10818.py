#N個の整数が与えられたとき、最小値と最大値を求めよう
#sorted() : 既存のListは変わらない
#sort() : 既存のListを変更

N = int(input())
list_val = list(map(int,input().split()))
print(f"{min(list_val)} {max(list_val)}")