import sys

N = int(sys.stdin.readline())
num_list = []

while N >0 :
    num_list.append(sys.stdin.readline().rstrip())
    N-=1

num_list.sort()
print("\n".join(num_list))