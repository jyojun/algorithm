n = int(input())

while n >= 10:
    if n % 10 == 0:
        n = int(n/10)
        continue

    else:
        print(n%10, end="")
        n = int(n/10)

print(n, end="")