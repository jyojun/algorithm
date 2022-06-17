def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        num = bin(arr1[i] | arr2[i])[2:]  # OR 연산 후  이진수로 변경
        if len(num) < n:
            num = '0'*(n-len(num)) + num
        ans = ["#" if n == '1' else ' ' for n in num]
        ans = ''.join(ans)
        answer.append(ans)
    return answer
