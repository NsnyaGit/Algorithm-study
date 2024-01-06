#自然数MとNが与えられた時、M以上N以下の自然数の中で素数である数字を全て選んで、
#この素数達の合と最小値を探すプログラムを作成

M = int(input())
N = int(input())


prime_num_list = []

for i in range(M,N+1):
    factor_cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            factor_cnt+=1
    if factor_cnt == 2:
        prime_num_list.append(i)

if len(prime_num_list) == 0:
    print(-1)
else:
    print(sum(prime_num_list))
    print(min(prime_num_list))

