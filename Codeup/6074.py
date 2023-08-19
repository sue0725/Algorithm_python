# 임의의 알파벳을 입력받음
c = ord(input())
# t에 a라는 알파벳을 저장
t = ord("a")

# t가 입력받은 c보다 작을 경우 t+1을 하며 c까지 출력한다 ''는 공백을 의미
while t <= c:
    print(chr(t), end=' ')
    t = t+1
