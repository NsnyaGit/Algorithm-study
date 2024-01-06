#配列Aが与えられた時、N番目に大きい数字を出力せよ。Aの大きさは１０であり、自然数のみ持っている。Nはいつも3

T = int(input())

while T >0:
    check_array =list(map(int, input().split()))
    print(sorted(check_array)[-3])
    T-=1