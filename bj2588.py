#https://www.acmicpc.net/problem/2588

a = int(input())
b = input()

for i in range(1,len(b)+1):
    print(a * (int(b[-i])))
print(a*int(b))