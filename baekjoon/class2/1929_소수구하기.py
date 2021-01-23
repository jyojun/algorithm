import sys
input = sys.stdin.readline

start, end = map(int, input().split())

result = [1 for _ in range(1000001)] #모든 인덱스의 수를 1로 저장

def isPrime(start, end):
    for i in range(2, end+1): #2부터 number 까지 수 반복 @start 부터 할 경우 앞에서 소수를 빼먹을 수 있음.
        if result[i] == 0: #이미 0인경우는 넘어감
            continue
        for j in range(i*2, end+1, i):
            result[j] = 0

    for i in range(start, end+1):
        if result[i] != 0:
            print(i)

isPrime(start, end)