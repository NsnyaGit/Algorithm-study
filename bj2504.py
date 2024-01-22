#https://www.acmicpc.net/problem/2504

from collections import deque

sign = input()
stack = deque()
ans = 0
tmp = 1

for i in sign:
    if i == '(':
        stack.append(i)
        tmp *= 2
    elif i == '[':
        stack.append(i)
        tmp *= 3
    elif i == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break  
        stack.pop()
        if not stack:
            ans += tmp
            tmp = 1
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        stack.pop()
        if not stack:
            ans += tmp
            tmp = 1