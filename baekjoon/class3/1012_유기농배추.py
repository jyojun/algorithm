import sys

input = sys.stdin.readline

N = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    farm[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or nx>=a or ny<0 or ny>=b:
            continue
        if farm[nx][ny] == 1:
            dfs(nx,ny)

for i in range(N):
    a,b,x = map(int, input().split())

    farm = [[0] * b for i in range(a)]
    count = 0

    for i in range(x):
        x,y = map(int, input().split())
        farm[x][y] = 1

    for i in range(a):
        for j in range(b):
            if farm[i][j] == 1:
                dfs(i,j)
                count += 1
    #print(farm) #모두 0이 되었는지 확인
    print(count)