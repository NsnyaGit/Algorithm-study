#整数AとBが与えられた時、AとBを比較するプログラムを作りなさい

A,B = map(int, input().split())


if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print("==")
