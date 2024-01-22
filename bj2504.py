#https://www.acmicpc.net/problem/2504

import sys
from collections import deque


sign = sys.stdin.readline().rstrip("\n")
stack = deque()
check_val = 0
is_valid = 1
#올바른 괄호열인지 판단
for i in sign:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        if len(stack) == 0:
            is_valid = 0
            break
        check_val = stack.pop()
        if i == ')':
            if check_val != '(':
                is_valid = 0
                break
        elif i == ']':
            if check_val != '[':
                is_valid = 0
                break
if len(stack) != 0:
    is_valid = 0

#괄호열 계산
