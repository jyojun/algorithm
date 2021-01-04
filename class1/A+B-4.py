a=b=1
while True:
    try:
        if a>0 and b<10:
            a, b = map(int, input().split())
            print(a+b)
    except:
        break

# 테스트 케이스 개수가 정해지지 않은경우에는 try-except 문 사용! 