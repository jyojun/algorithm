import sys

input = sys.stdin.readline

T = int(input())
result = 0

for x in range(T):
    numbers = list(map(int, input().split()))
    for i in range(10):
        if numbers[i] % 2 != 0:
            result += numbers[i]
    print(f'#{x+1} {result}')
    result = 0