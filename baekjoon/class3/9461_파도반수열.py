import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())

    p = [0, 1, 1, 1, 2, 2] # 1, 1, 1, 2, 2

    if N >= 6: 
        for j in range(6, N+1):
            p.append(p[j-1] + p[j-5])
    print(p[N])