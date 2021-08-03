import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
min_val = numbers[0]

for i in range(N):
    if min_val > numbers[i]:
        min_val = numbers[i]

count = 0

for i in range(N):
    if min_val == numbers[i]:
        count += 1

print(min_val, count)