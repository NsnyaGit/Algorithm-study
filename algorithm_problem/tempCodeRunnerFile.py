
# arr = [True] * 10000
# sample = int(10000**0.5) ## 에라토스테네스의 체 특성 n 은 n의 루트개 안에 있는 소수로만 나눠봐도 다 걸러짐

# for i in range(2, sample+1):
#     if arr[i] == True:
#         for j in range(i*2 , 10000, i):
#             arr[j] = False
# prime_num_list = [ i for i in range(2,10000) if arr[i]==True]
