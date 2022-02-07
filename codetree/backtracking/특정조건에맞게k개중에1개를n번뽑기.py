import sys

input = sys.stdin.readline

K, N = map(int, input().split())

answer = []

def Print():

    for i in range(len(answer)):
        print(answer[i], end=" ")
    print()

def conditional_seq(x):

    if x == N:
        Print()
        return

    for i in range(1, K+1):
        # i가 이전에 나온 2개의 숫자와 동일할 때 
        if x >= 2 and i == answer[-1] and i == answer[-2]:
            continue
        else:
            answer.append(i)
            conditional_seq(x+1)
            answer.pop()

conditional_seq(0)