#正数の整数nが与えられた時、これを二進数に表した時に１の位置を全て探すプログラムを作成
#LSBの位置は０である


T = int(input())

for i in range(0,T):
    cnt = 0
    result = []
    N = int(input())

    while N > 0:
        if N%2 == 1:
            result.append(cnt)
        N //= 2
        cnt+=1

    print(" ".join(map(str,result)))