#https://www.acmicpc.net/problem/2941

incoding_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for i in incoding_list:
    word = word.replace(i, "a")

print(len(word)) 
