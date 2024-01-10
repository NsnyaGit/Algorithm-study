#https://www.acmicpc.net/problem/4673

def d(n):
    ret_val = n + n%10 + (n%100)//10 + (n%1000)//100 + n//1000
    return ret_val 

check_list = [True] * 10001

for i in range(1, 10000):
    ret = d(i)
    if ret <= 10000:
        check_list[ret] = False

for i in range(1,10001):
    if check_list[i] == True:
        print(i)
    