def is_VPS(A):
    stack = []
    for i in range(len(A)):
        if A[i] == "(":
            stack.append(A[i])
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
                continue
        #print(stack)
    if len(stack)!=0:
        return False
    return True

n = int(input())
result = []
for i in range(n):
    temp = input()
    result.append(temp)

for i in result:
    if is_VPS(i):
        print("YES")
    else:
        print("NO")