import sys

input = sys.stdin.readline

n = int(input())

fx = [0] + list(map(int, input().split()))
dp = [[fx[x]] for x in range(n+1)]

# dp를 sparse table로 구현한다.
# k가 합성 횟수를 나타낸다.
# dp[n] = dp[dp[n][1]][1], dp[dp[n][2]][2], ... , dp[dp[n][19][19]]

# 시간복잡도 O(19*n) => O(n)을 갖는다.
for j in range(1, 19):  # k를 충분히 큰 수 2^19승까지 저장
    for i in range(1, n+1):  # k=1,2,4, ,,, 2^19 까지 각각 x=1~n에 저장
        dp[i].append(dp[dp[i][j - 1]][j - 1])
# print(dp)

q = int(input())  # 질의 수

# 질의의 수 만큼 합성함수를 반복하여 구한다.
for i in range(q):
    x, k = map(int, input().split())
    for j in range(18, -1, -1):
        if k >= 1 << j:  # k 값을 가장 큰 2^18 부터 2^0까지 살펴보아서 이진법 수에서 1인 숫자만큼 합성함수 dp에서 x를 업데이트 해준다.
            k -= 1 << j
            x = dp[x][j]
    print(x)  # 가장 마지막에 업데이트 된 x를 출력한다.

# 위 질의 반복문에서는 가장 큰 수를 2^18으로 두어 O(18q) 만큼 시간복잡도가 걸렸지만, k가 충분히 크다면
# 시간 복잡도 O(qlogk) 만큼 걸렸을 것 이다. 따라서 전처리 과정까지 합하면 O(n+qlogk) 이다.
