import sys

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [ list(map(int, input().split())) for _ in range(n) ]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

drs, dcs = [0, 1], [1, 0]

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < m

def DFS(r, c):
    
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        if in_range(nr, nc) == True:
            if not visited[nr][nc] and grid[nr][nc] == 1:
                visited[nr][nc] = 1
                DFS(nr, nc)

visited[0][0] = 1
DFS(0, 0)

print(visited[n-1][m-1])