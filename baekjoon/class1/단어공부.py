word = input()
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_list = []
for i in range(len(word)):
    temp = ord(word[i])
    if ord(word[i])>=97:
        temp = ord(word[i])-32
    
    temp = chr(temp)
    for j in alphabet:
        if temp == j:
            new_list.append(temp)
    #if alphabet[i]==temp:
     #   new_list.append(word.count(temp))
count_list = []
for i in alphabet:
    if i in new_list:
        count_list.append(new_list.count(i))
    else:
        count_list.append(0)
if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(chr(count_list.index(max(count_list))+65))