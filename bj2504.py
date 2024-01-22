#https://www.acmicpc.net/problem/2504

import sys
from collections import deque


sign = sys.stdin.readline().rstrip("\n")
stack = deque()


#올바른 괄호열인지 판단

for i in sign:
    print(i)