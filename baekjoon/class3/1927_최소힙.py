import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)

for i in range(N):
    order = int(input())

    if order == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    
    else:
        heapq.heappush(heap, order)