#アルファベットの小文字でできたN個の単語が入ってくると下の条件によってソートするプログラム作成
#1. lengthが短い順に
#2. lengthが同じだったら辞書に出てくる順に
#3. 被った単語は一つだけ残す

import sys
N = int(sys.stdin.readline()) # input보다 훨씬 빠름 맨 뒤 개행문자 조심 !
word_list = []
while N > 0:
    word_list.append(sys.stdin.readline())
    N-=1

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key = lambda word_len : len(word_len))

print("".join(word_list))



# 안 좋은 방법 ( 노가다 방법)
# for i in range(1,51): #i : 문자열 길이
#     for j in word_list:
#         if len(j) == i:
#             print(j)