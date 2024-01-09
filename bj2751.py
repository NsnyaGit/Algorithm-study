import sys

N = int(sys.stdin.readline())
num_list = []

while N >0 :
    num_list.append(int(sys.stdin.readline()))
    N-=1

num_list.sort()

num_list = list(map(str,num_list))
print("\n".join(num_list))