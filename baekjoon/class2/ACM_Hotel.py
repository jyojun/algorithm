t = int(input())
result = ''
for i in range(t):
    h,w,n = map(int,input().split())
    a = n // h + 1
    b = n % h
    if b == 0:
        b=h
        a-=1
    if a < 10:
        result = str(b) + '0' + str(a)
    else:
        result = str(b) + str(a)
    print(result)