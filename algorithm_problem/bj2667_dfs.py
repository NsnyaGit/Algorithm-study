import sys
input = sys.stdin.readline
n = int(input())
graph = [(list(map(int,(list(input().rstrip("\n")))))) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(graph,x,y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n : return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph,nx,ny)
        return True
    return False
            


result = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(graph,i,j) == True:
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)

    