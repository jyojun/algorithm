import sys

input = sys.stdin.readline

T = int(input())
L = int(input())

road = [[0] * (T+1) for i in range(T)]
visited = [0 for i in range(T)]
for i in range(L):
    a,b = map(int, input().split())
    road[a-1][b-1]=1
    road[b-1][a-1]=1

def dfs(v):
    visited[v]=1
    for i in range(T):
        if road[v][i] == 1 and visited[i] == 0: #길이 있고 방문하지 않았다면
            dfs(i)
dfs(0)
count = 0
for i in range(1,T):
    if visited[i]==1:
        count+=1
print(count)