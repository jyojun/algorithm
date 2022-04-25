import sys
input = sys.stdin.readline

N = map(int, input().split())
A = list(map(int, input().split()))

def solve(N, A):
	result = [0]
	stack = [A[0]]
	
	for i in range(1, len(A)):
		
		# 오른쪽보다 왼쪽이 클 경우 그냥 바로 왼쪽값을 저장: O(1)
		if A[i] > A[i-1]:
			result.append(A[i-1])
			stack.append(A[i])
		
		# 오른쪽보다 왼쪽이 클 경우
		else:
			
			# 스택의 꼭대기가 A[i] 보다 작다면 result에 저장: O(1)
			if stack[-1] < A[i]:
				result.append(stack[-1])
			
			# 스택의 꼭대기가 A[i] 보다 클 경우
			else:
				# 스택을 A[i]보다 작은 수가 나올 때 까지 계속 pop : 평균 O(1), 최악 O(N)
				while stack: 
					stack.pop() # 먼저 pop을 하고 
					if len(stack) == 0: # 스택이 비어있다면 A[i] 보다 작은 수가 없기 때문에 0을 저장
						stack.append(A[i])
						result.append(0)
						break
					
					# 스택 꼭대기에 A[i] 보다 작은 수가 나온다면 result에 저장 
					if stack[-1] < A[i]:
						result.append(stack[-1])
						stack.append(A[i])
						break
			
		#print("result:", result, "stack:",stack)
			
	return result

# for문을 N번만큼 돌고 각각 평균 O(1)씩 돌기때문에 전체 시간복잡도 : 평균 O(N)이다. 

for i in solve(N,A):
	print(i, end=" ")