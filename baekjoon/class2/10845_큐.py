import sys

input = sys.stdin.readline

n = int(input())
queue = []
for i in range(n):
    temp = list(input().split())
    if temp[0] == 'push':
        queue.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(queue) <= 0:
            print(-1)
        else:
            x = queue.pop(0)
            print(x)
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'empty':
        if len(queue) <= 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'front':
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) <= 0:
            print(-1)
        else:
            print(queue[len(queue)-1])