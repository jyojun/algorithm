max_num = 0
max_index = 0

for i in range(9):
    num = int(input())
    if max_num < num:
        max_index = i
        max_num = num

print(max_num)
print(max_index+1)