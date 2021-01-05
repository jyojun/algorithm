n, x = map(int, input().split())
num_list = [int(x) for x in input().split()]
new_list = []
for i in num_list:
    if i < x:
        new_list.append(i)
for i in range(len(new_list)):
    if i==len(new_list)-1:
        print(new_list[i], end="")
    else:
        print(new_list[i], end=" ")