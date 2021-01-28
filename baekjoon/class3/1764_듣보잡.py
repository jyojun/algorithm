import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hear = []
see = []
result = []
for i in range(N):
    word = input().strip()
    hear.append(word)

for i in range(M):
    word = input().strip()
    see.append(word)

if N>M:
    for i in range(N):