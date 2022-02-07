import sys

input = sys.stdin.readline

n = int(input())

grid = [ list(map(int, input().split())) for _ in range(n) ]
visited = [ [ 0 for _ in range(n) ] for _ in range(n) ]

people_num = 0
people_nums = list()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):

    if in_range(x,y) == False:
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    global people_num

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            people_num += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if(can_go(i, j)):

            visited[i][j] = 1
            people_num = 1

            dfs(i,j)

            people_nums.append(people_num)

#print(people_nums)
people_nums.sort()

print(len(people_nums))
for i in range(len(people_nums)):
    print(people_nums[i])