import sys
n = int(sys.stdin.readline())

lst = []
ans = []
for i in range(n):
    num = sys.stdin.readline().rstrip("\n")
    lst.append(num)

lst.sort(reverse=True)
ans.append(lst[0])
for i in range(1, len(lst)):
    tmp = 0
    for j in ans:
        if lst[i] == j[0:(len(lst[i]))]:
            tmp = 1
            break
    if tmp == 0: ans.append(lst[i])
        

print(len(ans))
