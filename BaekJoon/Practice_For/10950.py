# t에 임의의 정수를 입력받음 (테스트를 진행할 수)
t = int(input())

# t까지 도달할 때 까지
for i in range(t):
    # a,b에 숫자를 입력 받고 a+b를 출력한다
    a,b = map(int,input().split())
    print(a+b)
