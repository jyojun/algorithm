import sys

input = sys.stdin.readline 

N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]
visited = [0] * N

for i in range(M):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

count = 0

def dfs(v):
    global visited, graph
    visited[v] = 1
    for i in range(N):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

for i in range(N):
    if visited[i] == 0:
        dfs(i)
        count+=1

print(count)