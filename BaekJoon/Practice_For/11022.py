t = int(input())
x = 0

for i in range(1, t+1):
    a,b = map(int,input().split())
    x = x+1
    print("Case #" + str(x) + ":", a ,"+" ,b , "=", a+b)
