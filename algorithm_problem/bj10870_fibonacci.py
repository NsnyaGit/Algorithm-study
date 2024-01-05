#nが与えられた時、n番目のfibonacci数を求めるプログラムを作成

def fibonacci(n):
    ret_val = 0
    if n == 0:
        return ret_val
    elif n == 1:
        ret_val = 1
        return ret_val
    else:
        tmp = 0
        tmp1 = 1
        while n >= 2:
            ret_val = tmp1 + tmp
            tmp = tmp1
            tmp1 = ret_val

            n-=1
        return ret_val



n_of_seq = int(input())
print(fibonacci(n_of_seq))
