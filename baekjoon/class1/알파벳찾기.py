s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count_list = []
print(s.index('a'))
for i in alphabet:
    if i in s:
        count_list.append(s.index(i))
    else:
        count_list.append(-1)

for i in range(len(count_list)):
    if i==len(count_list)-1:
        print(count_list[i],end="")
    else:
        print(count_list[i],end=" ")