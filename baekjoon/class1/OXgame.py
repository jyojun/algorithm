n = int(input())

plus = 1

for i in range(n):
    score = input()
    result = 0
    plus = 1
    for j in score:
        if j == 'O':
            result += plus
            plus += 1
        elif j == 'X':
            plus = 1
        else:
            print("error")
    print(result)