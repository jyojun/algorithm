s = input()
alphabet='abcdefghijklmnopqrstuvwxyz'
new_list=[]
for i in alphabet:
    if i == 'z':
        print(s.find(i), end="")
    else:
        print(s.find(i),end=" ")