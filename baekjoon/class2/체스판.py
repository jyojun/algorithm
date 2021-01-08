def count_chess(n, m):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[n][m] == "W":
                if (i+n+j+m) % 2 == 0:
                    if board[i+n][j+m] == "B":
                        count+=1
                    else:
                        continue
                else:
                    if board[i+n][j+m] == "W":
                        count+=1
                    else:
                        continue
            else:
                if (i+n+j+m) % 2 == 0:
                    if board[i+n][j+m] == "W":
                        count+=1
                    else:
                        continue
                else:
                    if board[i+n][j+m] == "B":
                        count+=1
                    else:
                        continue
    count2 = 0
    for i in range(8):
        for j in range(8):
            if board[n][m] == "B":
                if (i+n+j+m) % 2 == 0:
                    if board[i+n][j+m] == "B":
                        count2+=1
                    else:
                        continue
                else:
                    if board[i+n][j+m] == "W":
                        count2+=1
                    else:
                        continue
            else:
                if (i+n+j+m) % 2 == 0:
                    if board[i+n][j+m] == "W":
                        count2+=1
                    else:
                        continue
                else:
                    if board[i+n][j+m] == "B":
                        count2+=1
                    else:
                        continue
    return min(count, count2)

n, m = map(int, input().split())
board = []

for i in range(n):
    temp = input()
    board.append(temp)
result = []
for i in range(n-8+1):
    for j in range(m-8+1):
        result.append(count_chess(i,j))
        #print(i,j)
print(min(result))
