#https://www.acmicpc.net/problem/2667

from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph,x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    
