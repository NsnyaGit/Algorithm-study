#bin()function を使用して解決

T = int(input())

for i in range(0,T):
    num = bin(int(input()))[2:]
    for i in range(len(num)):
        if num[-i-1] == '1':
            print(i, end=" ")
