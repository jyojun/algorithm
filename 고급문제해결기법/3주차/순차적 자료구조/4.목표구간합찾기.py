import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

def solve(n,k,A):
	sum = 0
	sum_queue = deque([]) # 큐를 생성한다. 
	for a in A:
		
		# 왼쪽에서 오른쪽으로 하나씩 추가해서 sum을 check한다. O(1)
		sum += a
		sum_queue.append(a) 
		
		# 원소 한개씩 추가할 때 마다 sum이 k보다 크면 작거나 같아질 때 까지 queue에서 하나씩 빼준다. 평균 O(1), 최악 O(N)
		while sum > k:
			temp = sum_queue.popleft()
			sum -= temp
			
		# 값이 k 가 되면 True로 출력
		if sum == k:
			return True
	
	# 반복문에 모두 돌 때 까지 없다면 False
	return False

# 총 알고리즘 함수의 시간복잡도: O(N) (for문 N번안에 평균 시간복잡도 각각 O(1)이므로 )
print(solve(n,k,A))