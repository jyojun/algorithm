# 우선순위 큐 (heapq로 구현)
import sys, heapq

input = sys.stdin.readline

T = int(input())
visited=[False]*1_000_001

for i in range(T):
    order_number = int(input())
    min_heap = []
    max_heap = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for i in range(order_number):
        order, number = map(str, input().split())
        number = int(number)
        
        # 최대, 최소힙을 동기화할 때 필요한 id값도 튜블에 넣어준다.
        if order == 'I':
            heapq.heappush(min_heap, [number, i])
            heapq.heappush(max_heap, [-number, i])
            visited[i] = True

        elif order == 'D':
            # 최댓값 삭제
            if number == 1:
                # max_heap이 존재하고, 그 부분에 False를 모두 삭제해준다. (동기화 과정)
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                # max_heap이 남아있다면(max값) 삭제해준다! (동기화 후 삭제)
                if max_heap:
                    visited[max_heap[0][1]]=False
                    heapq.heappop(max_heap)

            # 최솟값 삭제
            else:
                # min_heap이 존재하고, 그 부분에 False(이미 삭제된 값)을 모두 삭제 해 준다. 
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]]=False
                    heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if(len(min_heap) == 0 or len(max_heap) == 0):
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])