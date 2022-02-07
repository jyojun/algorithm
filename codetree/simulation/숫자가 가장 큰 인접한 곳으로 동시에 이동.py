import sys

input = sys.stdin.readline

# 격자 크기, 구슬 갯수, 시간
n, m, t = map(int, input().split())

grid = [ list(map(int,input().split())) for _ in range(n) ]

count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

next_count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 범위가 격자 안에 들어가는지 확인하는 함수
def in_range(x, y):
    return 0 <= x and x < n and 0<= y and y < n

# 인접한 곳들 중 가장 값이 큰 위치를 반환
def get_max_neighbor_pos(x, y):

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 우선순위 순서

    max_num, max_pos = 0, [0,0]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy

        # 최댓값 갱신 (상하좌우 우선순위 순으로 !)
        if in_range(next_x, next_y) and grid[next_x][next_y] > max_num:
            max_num = grid[next_x][next_y]
            max_pos = [next_x, next_y]
    
    return max_pos

# 다음 위치로 갈 구슬위치에 count 1씩 더해줌
def move(x, y):

    nx, ny = get_max_neighbor_pos(x, y)

    next_count[nx][ny] += 1

# 구슬의 위치를 모두 옮긴다.
def move_all():

    # 현재 위치의 구슬 갯수를 초기화
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    
    # 구슬이 있는 곳에서 움직인다. 그 움직임을 next_count에 기록
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    
    # next_count 값을 count에 복사. 
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

# count 자리에 2개이상이 있는 경우 지워준다 (충돌하는 경우)
def remove_ball():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0

# 시뮬레이션을 돌려줄 함수
def simulate():

    #구슬을 전부 한번씩 움직임.
    move_all()

    #움직인 후 지워줌
    remove_ball()

#초기 count 배열 설정
for i in range(m):
    x, y = tuple(map(int, input().split()))
    x, y = x-1, y-1 # 인덱스 번호는 1 작다.
    count[x][y] += 1

# t 시간만큼 시뮬레이션을 돌림
for i in range(t):
    simulate()

# count 값을 모두 더해줌
cnt = 0

for i in count:
    for j in i:
        cnt += j

print(cnt)