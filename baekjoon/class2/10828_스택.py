import sys

def push(x, A):
    A.append(x)

def pop(A):
    if len(A) <= 0:
        print(-1)
    else:
        x = A.pop()
        print(x)

def size(A):
    print(len(A))

def empty(A):
    if len(A) <= 0:
        print(1)
    else:
        print(0)

def top(A):
    if len(A) <= 0:
        print(-1)
    else:
        print(A[len(A)-1])

input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    temp = list(input().split())
    if temp[0] == 'push':
        stack.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(stack) <= 0:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif temp[0] == 'size':
        print(len(stack))
    elif temp[0] == 'empty':
        if len(stack) <= 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[len(stack)-1])