t = int(input())
x = 0
for i in range(1, t+1):
    a,b = map(int,input().split())
    x = x + 1
    # 공백을 없애기 위해 int가 아닌 str으로 출력
    # 문장 연결은 + 로
    print("Case #"+str(x)+":" ,a+b)
