import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().split())

A = list(map(int, input().split()))
interval = deque([]) # interval을 크기 k deque 사용
result = []

for i in range(len(A)):
	
	# k크기 구간 deque에 원소가 존재하고, interval 가장 위쪽의 값이 A[i]보다 작을 때까지 interval 가장 오른쪽 pop : 평균 O(1), 최악 O(N)
	while interval and interval[-1][1] > A[i]:
		interval.pop()
	
	''' k크기 구간 deque에 원소가 존재하고, interval 가장 왼쪽의 값이 원소값을 비교할 때, 
	interval k크기에서 빠져나가면 가장 왼쪽을 pop : 평균 O(1), 최악 O(N) '''
	while interval and (i - interval[0][0] >= k):
		interval.popleft()
	
	# pop 과정이 끝났다면 A[i]을 interval 오른쪽에 추가 : O(1)
	interval.append([i, A[i]])
	
	# k-1 번째 원소차례 일 때 부터 result에 추가한다. (그 전 원소는 interval 크기만큼 가지 않았기 때문) : O(1) 
	if i >= (k-1):
		result.append(interval[0][1])

# for 문을 N번 도는 동안 각각 평균 O(1)번씩 돌기 때문에, 전체 시간복잡도 : O(N)
for r in result:
	print(r, end=" ")	