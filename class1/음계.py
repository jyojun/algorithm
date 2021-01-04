list1 = list(map(int, input().split()))

ascending = False
descending = False
mixed = False

for i in range(len(list1)-1):
    if list1[0] < list1[1]:
        if list1[i] > list1[i+1]:
            mixed = True
        ascending = True
    else:
        if list1[i] < list1[i+1]:
            mixed = True
        descending = True

if mixed:
    print("mixed")
else:
    if ascending:
        print("ascending")
    elif descending:
        print("descending")
    else:
        print("error")
        