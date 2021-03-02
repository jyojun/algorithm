import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for i in range(N)]
blue = 0
white = 0

#print(paper)

def cut(x,y,N):
    global blue, white
    check = paper[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if check != paper[i][j]:
                cut(x,y,N//2)
                cut(x+N//2,y,N//2)
                cut(x,y+N//2,N//2)
                cut(x+N//2,y+N//2,N//2)
                return

    if check==0:
        white+=1
        return
    else:
        blue+=1
        return

cut(0,0,N)
print(white)
print(blue)
