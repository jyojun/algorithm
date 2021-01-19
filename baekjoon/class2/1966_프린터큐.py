import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for i in range(N):
    N, M = map(int, input().split())
    count = 0
    queue = deque(list(map(int, input().split())))
    
    while count <= N:
        if M == 0:
            if queue[M] == max(queue):
                queue.popleft()
                count += 1
                print(count)
                break
            else:
                temp = queue.popleft()
                queue.append(temp)
                
                M -= 1
                if M < 0:
                    M = len(queue)-1

        else:
            if queue[0] == max(queue):
                queue.popleft()
                count+=1
                M -= 1
                if M < 0:
                    M = len(queue)-1
            else:
                temp = queue.popleft()
                queue.append(temp)
                M -= 1
                if M < 0:
                    M = len(queue)-1
        #print(queue)