# import sys

# input = sys.stdin.readline

# N = int(input())

# result = 1
# for i in range(2,N+1):
#     result *= i

# count = 0
# for i in range(len(str(result))):
#     if result % 10 == 0:
#         count += 1

#     result /= 10

# print(count)

import math

n = int(input())
n_factorial = str(math.factorial(n))  # n!
cnt = 0

for i in range(len(str(n_factorial))-1, 0, -1):
    if n_factorial[i] == '0':
        cnt += 1
    else:
        break
print(cnt)