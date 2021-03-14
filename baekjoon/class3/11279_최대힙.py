import sys
import heapq

input = sys.stdin.readline

N = int(input())

h = []

for i in range(N):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -x)