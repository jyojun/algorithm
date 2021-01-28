import sys
input = sys.stdin.readline

N = int(input())
stack = []
count = 1
result = []
chance = True
for i in range(N):
    number = int(input())
    while count <= number:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[len(stack)-1] == number:
        #print(stack[len(stack)-1])
        stack.pop()
        result.append('-')
    else:
        chance = False
    #print(stack)

if chance:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")