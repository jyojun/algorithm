a=b=1
while a>0 and b<10:
    a, b = map(int, input().split())
    if not (a>0 and b<10):
        break
    print(a+b)

