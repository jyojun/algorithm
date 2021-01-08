def solution(board, moves):
    stack = []
    count = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break
        if len(stack) >= 2:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop()
                stack.pop()
                count += 2
    return count