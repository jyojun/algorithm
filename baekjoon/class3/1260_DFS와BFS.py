import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(v):
    visited = [0] * (N+1)
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[v])):
            if graph[v][w] == 1 and visited[w] == 0:
                visited[w] = 1
                queue.append(w)

visited2 = [0] * (N+1)
def dfs(v):
    visited2[v] = 1
    print(v, end=' ')

    for w in range(len(graph[v])):
        if graph[v][w] == 1 and visited2[w] == 0:
            dfs(w)

dfs(V)
print()
bfs(V)