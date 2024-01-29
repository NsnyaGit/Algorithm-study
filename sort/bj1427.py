import sys
num = list(sys.stdin.readline().rstrip('\n'))
print("".join(sorted(num, reverse=True)))