import math

def is_prime(k):
    if k == 1:
        return False
    for i in range(2, int(math.sqrt(k))+1):
        # k가 해당 수로 나누어 떨어진다면
        if k % i == 0:
            return False
    return True

def k_number(k, n):
    result = ""
    
    while n != 0:
        result += str(n % k)
        n = int(n/k)
    return result[::-1]

def solution(n, k):
    answer = 0
    
    k_num = k_number(k, n)
    
    k_num_list = k_num.split('0')
    print(k_num_list)
    for x in k_num_list:
        if x.isdecimal():
            if is_prime(int(x)):
                answer+=1
    
    return answer