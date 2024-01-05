#https://www.acmicpc.net/problem/2309

result = []
for i in range(9):
    result.append(int(input()))

sum_val = sum(result) - 100

for i in range(len(result)):
    check_val = sum_val - result[i]
    for j in range(i+1,len(result)):
        if check_val == result[j]:
            result.pop(j)
            result.pop(i)
            break
    if len(result) == 7:
        break

result.sort()
for i in result:
    print(i)