#2個の自然数の入力を受け、最大公約数と最小公倍数を出力するプログラムを作成

# using math library
# import math

# a,b = map(int,input().split())

# print(math.gcd(a,b))
# print(math.lcm(a,b))


a,b = map(int,input().split())

if a<=b:
    t = a
else:
    t = b

common_factor = [1]
the_least_common_multiple = 0
the_greatest_common_divisor = 1
while True:
    trg = 0
    for divisor in range(2,t+1):
        if a%divisor == 0 and b%divisor == 0:
            common_factor.append(divisor)
            a //= divisor
            b //= divisor
            if a<=b:
                t = a
            else:
                t = b
            trg = 1
            break
        
    if trg == 0:
        the_least_common_multiple = a*b
        break

for i in common_factor:
    the_least_common_multiple *= i
    the_greatest_common_divisor *= i
print(the_greatest_common_divisor)
print(the_least_common_multiple)
    