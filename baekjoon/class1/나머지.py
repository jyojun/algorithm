num_list = []
for i in range(10):
    num = int(input())
    num_list.append(num%42)
new_list = []
for i in num_list:
    if i in new_list:
        continue
    else:
        new_list.append(i)

print(len(new_list))