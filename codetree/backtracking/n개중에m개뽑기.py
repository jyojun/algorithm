import sys

input = sys.stdin.readline

result = []

N, M = map(int, input().split())

def Print():
    for i in range(len(result)):
        print(result[i], end=" ")
    print()

def permutation(x):

    if x == M:
        Print()

        return
    
    for i in range(1, N+1):
        if len(result) == 0:
            result.append(i)
            permutation(x+1)
            result.pop()
        else:
            if i > result[-1]:
                result.append(i)
                permutation(x+1)
                result.pop()
            else:
                continue

permutation(0)