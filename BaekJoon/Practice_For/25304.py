x = int(input()) # 총 금액
n = int(input()) # 물건 종류 수
total = 0

for i in range(n):
    a,b = map(int,input().split())
    total = total + (a*b)

if total == x:
        print("Yes")

elif total != x:
        print("No")


