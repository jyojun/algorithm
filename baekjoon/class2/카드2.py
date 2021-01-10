from collections import deque
n = int(input())
cards = []
for i in range(n,0,-1):
    cards.append(i)
queue = deque(cards)

while(len(queue)>1):
    queue.pop()
    queue.appendleft(queue.pop())
print(queue[0])

#디큐를 사용 (insert(0,queue.pop()) 은 O(N)으로 성능상으로 불리)
#appendleft()은 O(N) 의 시간복잡도를 갖는다.