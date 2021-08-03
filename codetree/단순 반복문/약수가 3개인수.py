import sys, math

input = sys.stdin.readline

start, end = map(int, input().split())

def is_prime_number(n):
    array = [True for i in range(n+1)]

    # 에라토스 테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i*j <= n:
                array[i * j] = False
                j += 1
    return array

count = 0
numbers = is_prime_number(end)
numbers[1] = False

for i in range(start, end+1):
    if i == int(math.sqrt(i)) ** 2:
        if numbers[int(math.sqrt(i))]:
            count += 1
            #print(i)    

print(count)

# 소수인 수의 제곱인 수 = 약수가 3개인 수