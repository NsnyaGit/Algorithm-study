#N個の数が与えられた時、これを昇順に整列するプログラムを作成

N = int(input())
result = []
for i in range(N):
    result.append(int(input()))

result.sort()
for i in result:
    print(i)    