T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())

    result = a + b
    if result >= 24:
        result -= 24
    
    print(f'#{i} {result}')