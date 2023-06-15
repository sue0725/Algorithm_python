# 자연수 입력

n,m,k = map(int,input().split())

# 데이터 입력

data = list(map(int, input().split()))

# 데이터 정렬

data.sort()

# 가장 큰 수와 두번째로 큰 수 도출

first = data[n-1]
second = data[n-2]

# 가장 큰 수 더해지는 횟수 도출

count = int(m / (k+1)) * k
count += m % (k+1)

# 가장 큰 수와 두번째로 큰 수 더하기

result = 0
result += (count) * first
result += (m-count) * second

print(result)