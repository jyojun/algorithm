import sys

x, y = 0, 0
dir_num = 3
dir = [[1,0], [-1,0], [0,-1], [0,1]]

def rotate_dir(dir_num, dir):
    if dir == 'R':
        if dir_num == 0:
            dir_num = 2
        elif dir_num == 1:
            dir_num = 3
        elif dir_num == 2:
            dir_num = 1
        else:
            dir_num = 0
    else:
        if dir_num == 0:
            dir_num = 3
        elif dir_num == 1:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 0
        else:
            dir_num = 1
    return dir_num

order = input()

for i in range(len(order)):
    if order[i] == 'L' or order[i] == 'R':
        dir_num = rotate_dir(dir_num, order[i])
    else:
        x, y = x + dir[dir_num][0], y + dir[dir_num][1]

print(x, y)