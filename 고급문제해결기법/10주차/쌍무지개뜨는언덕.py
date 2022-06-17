import sys

input = sys.stdin.readline

n, k = map(int, input().split())

rainbow = []
for i in range(n):
    rainbow.append(int(input()))

# print(rainbow)
map = {x: 0 for x in range(1, k+1)}	 # p'의 1~k count 값
map2 = {x: 0 for x in range(1, k+1)}  # p의 1~k count 값


# p는 처음에 모두 있기때문에, rainbow 전체의 원소를 count 한다
for x in rainbow:
    map2[x] += 1

# two pointer를 사용
start, end = 0, 0
result = []
cnt = 0  # p'의 원소 종류수
cnt2 = k  # p의 원소 종류수
# print(map)

while end < len(rainbow) and start <= end:

    # 처음에 현재 end값에 방문했으니 p'에 end 인덱스 저장
    map[rainbow[end]] += 1

    # p'에 의해 end자리 값을 뺐겼으니 end 인덱스 자리 count 한개 차감
    map2[rainbow[end]] -= 1

    # 원래 없었던 것 (0) 에서 한개가 된거라면 cnt 를 추가
    if map[rainbow[end]] == 1:
        cnt += 1

    # 1개밖에 없던것에서 0이 되어버렸다면 cnt2 를 차감
    if map2[rainbow[end]] == 0:
        cnt2 -= 1

    # 종류가 k개에서 차감되지 않을 때까지만 start를 전진한다.
    while(map[rainbow[start]] > 1):
        map[rainbow[start]] -= 1
        map2[rainbow[start]] += 1
        if map2[rainbow[start]] == 1:
            cnt2 += 1
        start += 1

    # print(map)
    # print(map2)

    # 둘다 종류가 k개 있다면 p'구간 크기를 저장 (쌍 무지개가 존재 한다는 의미)
    if cnt == k and cnt2 == k:
        result.append(end-start+1)

    # 모든 action을 한 후, end 한칸 전진
    end += 1

# 쌍무지개가 존재한 경우, p'구간의 크기의 최솟값을 출력
if result:
    print(min(result))
# 쌍무지개가 존재한 경우가 없다면 0을 출력
else:
    print(0)

# 최악의 경우 end, start 모두 n번 이동하는 경우이다. 2n번 이므로 시간복잡도는 O(n)이다.
