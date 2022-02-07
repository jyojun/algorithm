import sys
from itertools import accumulate

input = sys.stdin.readline

N, M = map(int, input().split())

#print(N, M)

numbers = list(map(int, input().split()))
sum_numbers = list(accumulate(numbers))
sum_numbers.insert(0, 0)
#print(numbers)

for i in range(M):
    x, y = map(int, input().split())
    print(sum_numbers[y] - sum_numbers[x-1])