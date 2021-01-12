import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    room = []
    a = int(input()) + 1 # 0층부터 시작하니 +1을 해준다
    b = int(input()) 

    for j in range(a):
        room.append([]) 
        for k in range(b):
            if j == 0:
                room[0].append(k+1)
            else:
                room_sum = 0
                for l in range(k+1):
                    room_sum += room[j-1][l]
                room[j].append(room_sum)
    print(room[a-1][b-1]) # 0~a-1층 , 0~b-1호 까지 생기므로 a층은 a-1, b호는 b-1