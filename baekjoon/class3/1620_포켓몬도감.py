import sys
input = sys.stdin.readline

N, M = map(int, input().split())
monsters = [input().strip() for _ in range(N)]
#print(monsters)

for i in range(M):
    temp = input().strip()

    if temp[0] >= '0' and temp[0] <= '9':
        print(monsters[int(temp)-1])
    else:
        print(monsters.index(temp)+1)