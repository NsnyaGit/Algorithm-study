#Little Ivan is bored at math class so he decided to play popular game called "Bomboni".
#At the beginning all fields of N×N square board contain candies (not necessarily of same color). 
#When its his turn player should swap two neighbouring (up, down, left or right) candies of different color 
#and then pick some sequence (in row or column) of same color candies which he will take and eat. 
#Initial board configuration is given, help Ivan and write a program which will calculate maximal number of candies he can win in the first move. 

import sys

def getMaxCandy(lst):
    ret = 0
    #가로
    for i in range(len(lst)):
        num = 1
        for j in range(len(lst)-1):
            if lst[i][j] == lst[i][j+1]:
                num+=1
            else:
                if num > ret: ret = num
                num=1
        if num > ret: ret = num
            
    #세로
    for i in range(len(lst)):
        num = 1
        for j in range(len(lst)-1):
            if lst[j][i] == lst[j+1][i]:
                num+=1
            else:
                if num > ret: ret = num
                num = 1
        if num > ret: ret = num
    return ret
    

N = int(sys.stdin.readline())

n_lst = []

while N > 0:
    candy = list(sys.stdin.readline().rstrip("\n"))
    n_lst.append(candy)
    N-=1

ret = 0
result = 1

# 가로
for i in range(len(n_lst)):
    for j in range(len(n_lst)-1):
        if n_lst[i][j] != n_lst[i][j+1]:
            tmp = n_lst[i][j]
            n_lst[i][j] = n_lst[i][j+1]
            n_lst[i][j+1] = tmp
            ret = getMaxCandy(n_lst)
            if result < ret: result = ret
            n_lst[i][j+1] = n_lst[i][j]
            n_lst[i][j] = tmp
ret = getMaxCandy(n_lst)
if result < ret: result = ret

# 세로
for i in range(len(n_lst)-1):
    for j in range(len(n_lst)):
        if n_lst[i][j] != n_lst[i+1][j]:
            tmp = n_lst[i][j]
            n_lst[i][j] = n_lst[i+1][j]
            n_lst[i+1][j] = tmp
            ret = getMaxCandy(n_lst)
            if result < ret: result = ret
            n_lst[i+1][j] = n_lst[i][j]
            n_lst[i][j] = tmp
ret = getMaxCandy(n_lst)
if result < ret: result = ret


print(result)