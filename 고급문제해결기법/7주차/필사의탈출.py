import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

# 위 두겹의 장벽의 구멍을 모두 입력받아 파이썬 sort 함수를 이용해 오름차순으로 정렬(2*nlogn)
num1 = int(input())
first_holes = list(map(int, input().split()))
first_holes.sort()

num2 = int(input())
second_holes = list(map(int, input().split()))
second_holes.sort()

# 시간복잡도 문제 때문에, 마지막 장벽은 모든 장벽 구멍의 경우의 수 크기만큼 리스트를 생성하여 정보를 받는다.
# 시간복잡도 대신 공간 복잡도(메모리 사용)가 증가
num3 = int(input())
last = [0 for x in range(-30000, 30001)]
third_holes = list(map(int, input().split()))

for third_hole in third_holes:  # 마지막 구멍의 위치를 리스트의 인덱스로 사용해 딕셔너리 형태로 저장.
    last[third_hole] = 1

cnt = 0
for first_hole in first_holes:
    for second_hole in second_holes:
        x = first_hole
        y = second_hole
        temp = x - y
        if temp < -30000:  # 오름차순으로 정렬이기 때문에, y가 x보다 30000이상 클 경우 마지막 구멍은 존재하지 않으므로 break
            break
        if last[y-temp]:  # x - y == y - z와 같은 z가 리스트에 존재하는지 check O(1)
            cnt += 1

print(cnt)

# 2개의 장벽을 탐색하는데 2중 for문을 사용했기 때문에 O(n^2)이고, 마지막 구멍이 첫번쨰 구멍과 두번째 구멍을 통과했을 때,
# 맞는 구멍인지 확인하는 작업은 리스트가 딕셔너리 형태로 인덱스에 접근하는 형식이므로 상수시간 소요되기 때문에
# 처음에 정렬하는 시간과 합쳐서 O(2nlogn + n^2) 이므로 => O(n^2)가 소요된다.
