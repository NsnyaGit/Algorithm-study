#(A+B)%Cは ((A%C) + (B%C))%C と等しいだろうか
#(A×B)%Cは ((A%C) × (B%C))%C と等しいだろうか
#A, B, Cが与えられた時, 上の四つのケースの答えを求めよう

a,b,c = map(int,input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)