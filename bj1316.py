#https://www.acmicpc.net/problem/1316

import sys

N = int(sys.stdin.readline())


cnt = 0

while N > 0:
    word = sys.stdin.readline().rstrip('\n')
    check = [True] * 27
    is_group_word = 1

    for i in range(len(word)):
        if check[ord(word[i]) - ord('a')] == True:
            check[ord(word[i]) - ord('a')] = False
        elif check[ord(word[i]) - ord('a')] == False:
            if word[i] != word[i-1]:
                is_group_word = 0
                break
    
    if is_group_word: cnt += 1
    N-= 1
print(cnt)