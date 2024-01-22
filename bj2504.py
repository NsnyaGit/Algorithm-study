#https://www.acmicpc.net/problem/2504


sign = input()
stack = []
ans = 0
tmp = 1

for i in range(len(sign)):
    if sign[i] == '(':
        stack.append(sign[i])
        tmp *= 2
    elif sign[i] == '[':
        stack.append(sign[i])
        tmp *= 3
    elif sign[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if sign[i-1] == '(':  
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if sign[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if not stack:
    print(ans)
else:
    print(0)