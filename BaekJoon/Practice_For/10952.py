# true 일 동안
while 1:
    #a,b를 입력받고 만약 a와 b가 0 일 경우 break
    a,b = map(int,input().split())
    if(a == 0 and b == 0):
        break
        # 아니라면 계속 출력
    else:
        print(a+b)