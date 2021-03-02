import sys

input = sys.stdin.readline

T = int(input())
L = int(input())

road = [[0] * (T+1) for i in range(T)]
visited = [0 for i in range(T)]
for i in range(L):
    a,b = map(int, input().split()) #연결할 노드 2개를 입력
    road[a-1][b-1]=1 #양방향 으로 모두 갈수 있기 때문에 양방향 둘 다 1로 저장한다. 
    road[b-1][a-1]=1

def dfs(v):
    visited[v]=1
    for i in range(T):
        if road[v][i] == 1 and visited[i] == 0: #길이 있고 방문하지 않았다면
            dfs(i)
dfs(0) #1번 컴퓨터에서 탐색시작
count = 0
for i in range(1,T):
    if visited[i]==1:
        count+=1
print(count)