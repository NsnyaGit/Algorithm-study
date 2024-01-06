#与えられた数字N個の中で素数が何個か出力するプログラムを作成

N = int(input())

rev_val = list(map(int,input().split()))
result_cnt = 0
factors = []
while N > 0:

    for i in range(1,rev_val[N-1]+1):
        if rev_val[N-1]%i == 0:
            factors.append(i)
    
    if len(factors) == 2:
        result_cnt+=1

    factors = []            
    N-=1

print(result_cnt)