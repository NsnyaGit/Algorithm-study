#get prime numbers using Sieve of Eratosthenes Algorithm

arr = [True] * 10000 #문제에서 제시된 자연수의 범위가 1~10000이기 때문에
divisor = int(10000**0.5) # 2~ 10000**0.5 까지의 값으로 나눠서 소수만 걸러냄

for i in range(2, divisor+1):
    if arr[i] == True:
        for j in range(i*2, 10000, i):
            arr[j] = False
prime_num_list = [i for i in range(2,10000) if arr[i]==True]

M = int(input())
N = int(input())

sum = 0
min_val = 0
for i in prime_num_list:
    if i < M:
        continue
    elif M <= i <= N :
        if min_val == 0:
            min_val = i        
        sum += i
    else:
        break
print(sum, min_val, sep = '\n') if sum != 0 else print(-1)