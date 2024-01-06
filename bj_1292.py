#https://www.acmicpc.net/problem/1292

start,end = map(int,input().split())

result = 0
for i in range(start,end+1):

    tmp = 0
    while i >0:
        tmp+=1
        i -= tmp
    
    result+=tmp

print(result)
