T = int(input())

def check(board, x, y):
    # 가로 체크
    if board[x][y] == 'o' and board[x][y+1] == 'o' and board[x][y+2] == 'o' and board[x][y+3] == 'o' and board[x][y+4] == 'o':
        return True
    
    # 세로 체크
    if board[x][y] == 'o' and board[x+1][y] == 'o' and board[x+2][y] == 'o' and board[x+3][y] == 'o' and board[x+4][y] == 'o':
        return True
    
    # 대각선 체크

    if board[x][y] == 'o' and board[x+1][y+1] == 'o' and board[x+2][y+2] == 'o' and board[x+3][y+3] == 'o' and board[x+4][y+4] == 'o':
        return True

    # 역대각선 체크 
    if board[x][y+4] == 'o' and board[x+1][y+3] == 'o' and board[x+2][y+2] == 'o' and board[x+3][y+1] == 'o' and board[x+4][y] == 'o':
        return True
    
    return False

result = False

for x in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    #print(board)

    for i in range(N-4):
        if result:
            break
        for j in range(N-4):
            if check(board, i, j):
                result = True
                #print('YES')
                break
            else:
                result = False
    if result:
        print(f'#{x} YES')
    else:
        print(f'#{x} NO')