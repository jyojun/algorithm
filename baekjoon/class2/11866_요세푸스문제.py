import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([])

for i in range(N):
    queue.append(i+1)
index = K
result = []

for i in range(N-1):
    
    for j in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
result.append(queue[0])

str_result = '<'+', '.join(str(i) for i in result)+'>'
print(str_result)
'''
1 2 3 4 5 6 7 8 9 10
index = 5 5
1 2 3 4 6 7 8 9 10
index = 9 10
1 2 3 4 6 7 8 9
index = 5 4
1 2 3 6 7 8 9
'''