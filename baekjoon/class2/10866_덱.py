import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dq = deque([])

for i in range(n):
    temp = list(input().split())
    if temp[0] == 'push_front':
        dq.appendleft(int(temp[1])) #deque 의 appendleft() 을 사용
    elif temp[0] == 'push_back':
        dq.append(int(temp[1]))
    elif temp[0] == 'pop_back':
        if len(dq) <= 0:
            print(-1)
        else:
            print(dq.pop())
    elif temp[0] == 'pop_front':
        if len(dq) <= 0:
            print(-1)
        else:
            print(dq.popleft()) #deque 의 popleft() 을 사용
    elif temp[0] == 'size':
        print(len(dq))
    elif temp[0] == 'empty':
        if len(dq) <= 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'front':
        if len(dq) <= 0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq) <= 0:
            print(-1)
        else:
            print(dq[len(dq)-1])