a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a == b == c: # 같은 눈 3개
    print(10000 + (a * 1000))

elif a == b or b == c: # 같은 눈 2개
    print(1000 + (b * 100))

elif a == c: # 같은 눈 2개(2)
    print(1000 + (c * 100))

else: # 모두 다른 눈
    print(max(a,b,c) * 100)