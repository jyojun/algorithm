import sys
from bisect import bisect_right, bisect_left # 이진탐색을 사용하는 python library bisect을 사용.
input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
	temp = int(input())
	nums.append(temp)
count = 0

nums.sort() # 파이썬의 sort()함수는 Tim Sort를 사용하며 평균 시간 복잡도는 O(NlogN) 이다.

# bisect_left(a, left) a 리스트에서 left값의 가장 왼쪽의 인덱스를 반환 이진탐색을 하여 평균 O(logN) 이 걸린다. 
# bisect_right(a, right) a 리스트에서 right값의 가장 오른쪽의 인덱스를 변환 이진탐색을 하여 평균 O(logN)이 걸린다.  

# 아래 구현한 함수는 bisect_left, bisect_right 함수를 각각 두번씩 썼기 때문에 O(2logN) 이 걸린다.
def left_to_right(nums, left_value, right_value):
	right = bisect_right(nums, right_value)
	left = bisect_left(nums, left_value)
	return right-left


# 문자열을 앞에 숫자(작은 숫자 a,b) 2개까지 고른 상태에서 이중 for문을 사용 평균 시간복잡도 O(N^2)이 걸리고
# c의 범위를 이용하여 O(2logN)이 걸리는 함수를 사용하면 총 O(2N^2 * logN) 시간복잡도가 생긴다.
for i in range(len(nums)-2):
	for j in range(i+1, len(nums)-1):
		diff = nums[j] - nums[i]
		count += left_to_right(nums, nums[j]+diff, nums[j]+2*diff) 
			
print(count)

# 삼중 for문을 사용하여 O(N^3) 에서는 4개의 테스트 케이스만 통과하였으나, 
# c값을 확인하는 과정에서 위 이진탐색을 사용하니 O(2N^2*logN) 시간복잡도으로 모든 테스트 케이스들이 통과하였다.