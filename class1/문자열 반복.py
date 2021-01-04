n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    c = ""
    if len(b) > 20:
        break
    for j in range(len(b)):
        c += (b[j]*a)
    print(c)