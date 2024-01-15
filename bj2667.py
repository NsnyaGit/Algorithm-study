#https://www.acmicpc.net/problem/2667

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph,x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    n = len(graph)
    queue = deque()
    queue.append((x,y))
    cnt = 1
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                cnt+=1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    
    return cnt

if __name__ == "__main__":
    N = int(input())
    graph = []
    result = []

    for i in range(N):
        graph.append(list(map(int,(list(input().rstrip("\n"))))))
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                result.append(bfs(graph,i,j))
    
    result.sort()
    print(len(result))
    for i in result:
        print(i)