#N個の数字が空白無しに与えられる。この数字を全部足して出力するプログラムを作成
#join() : 문자열반환
#split() : 리스트 반환

N = int(input())

values = input()
values = ",".join(values)
result_list = list(map(int,values.split(",")))
print(sum(result_list))