import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 인접행렬 생성
graph = [ [0 for _ in range(N+1)] for _ in range(N+1) ]

# 각 정점마다 방문 여부 
visited =[ False for _ in range(N+1) ]

def DFS(vertex):
    for i in range(1, N+1):

        # 연걸되어있고, 방문하지 않은 경우
        if graph[vertex][i] and visited[i] == False:
            visited[i] = True
            DFS(i)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

DFS(1)
#print(visited)

cnt = 0

for i in range(1, N+1):
    if visited[i] == True and i != 1:
        cnt += 1

print(cnt)