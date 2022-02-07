import sys

input = sys.stdin.readline

answer = []

k, n = map(int, input().split())

def Print():
    for i in range(len(answer)):
        print(answer[i], end=" ")
    print()

def Choose(curr_num):
    if(curr_num == n):
        Print()
        return

    for i in range(1,k+1):
        answer.append(i)
        Choose(curr_num + 1)
        answer.pop()
    
    return

Choose(0)
