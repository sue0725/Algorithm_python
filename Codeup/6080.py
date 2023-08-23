# 각기 다른 주사위 면 2개가 입력됨
n,m = map(int, input().split())

# 모든 경우의 수를 계산해야 하므로 이중 반복문을 사용해 1,1부터 n,m까지 출력
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)
