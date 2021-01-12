import sys
input = sys.stdin.readline
n = int(input())
word = input(n) # 마지막에 빈 문자열이 들어가기 때문에 문자열 길이 n 까지 받는다.
result = 0
#print(len(word)-1)

def power(x,y):
    if y == 0:
        return 1
    
    divide = power(x,y//2)

    if y%2==0:
        return divide * divide
    else:
        return divide * divide * x

for i in range(len(word)):
    result += (ord(word[i])-ord('a')+1)*power(31,i)

# 31**i 연산에서 O(N^2) 의 시간복잡도가 생기기 때문에, 시간초과
''' 
for i in range(len(word)):
    result += (ord(word[i])-ord('a')+1)*(31**i)
    #print(word[i])
'''
print(result%1234567891)