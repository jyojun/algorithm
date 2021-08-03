import sys

input = sys.stdin.readline

N = int(input())
students = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    students[i][0], students[i][1] = map(int, input().split())
    students[i][2] = i+1

# 키 큰순서(내림차순 음수) -> 몸무게 큰순서(내림차순 음수) -> 번호 작은순서(오름차순 양수)
students.sort(key = lambda x: (-x[0], -x[1], x[2])) 

for i in range(N):
    for j in range(3):
        print(students[i][j], end=" ")
    print()