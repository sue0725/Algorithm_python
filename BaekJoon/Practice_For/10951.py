while 1:
    # try except 활용하여 테스트케이스가 들어오지 않을 때(enter) 종료
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break
