import sys

n = int(sys.stdin.readline())


lst = []
ans = []
for i in range(n):
    num = sys.stdin.readline().rstrip("\n")
    lst.append(num)

lst.sort(reverse=True)
for i in range(len(lst)-1):
    for j in range(len(lst[i+1])):
        if lst[i][j] != lst[i+1][j]:
            break
        
