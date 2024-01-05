#https://www.acmicpc.net/problem/2460

n_of_people_on_board = 0
result = []
for i in range(10):
    m,p = map(int,input().split())
    n_of_people_on_board -= m
    n_of_people_on_board += p
    result.append(n_of_people_on_board)

print(max(result))
