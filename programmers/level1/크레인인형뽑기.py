def solution(board, moves):
    stack = []
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                print(board[j][moves[i]-1])
                stack.append(board[j][i])
                board[j][i]=0
                break
    answer = 0
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)

print(board)
print(stack)