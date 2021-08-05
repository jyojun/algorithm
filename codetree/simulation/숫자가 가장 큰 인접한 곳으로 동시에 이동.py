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
        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
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
            next_count