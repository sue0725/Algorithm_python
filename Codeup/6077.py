# 임의의 정수를 입력받음
n = int(input())
s = 0

# 1부터 n+1 까지 짝수 일 경우만 더함
for i in range(1, n+1):
    if i%2==0:
        s = s + i

print(s)