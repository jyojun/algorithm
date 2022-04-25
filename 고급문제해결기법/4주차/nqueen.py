import sys

input = sys.stdin.readline

# Queen1과 Queen2가 서로 잡을 수 없는 상태인지 확인
def check(Q1, Q2):
	if Q1[0] == Q2[0] or Q1[1] == Q2[1] or abs(Q1[1]-Q2[1]) == Q2[0]-Q1[0]:
		return False
	return True

# board를 돌 때 dfs 알고리즘을 사용한다. dfs를 돌면서 Q1, Q2를 저장한다 
def dfs(x, Q1, Q2):
	global count
	
	# x는 0부터 시작하고 N번 돌 때 까지 반복한다. O(N)
	if x == N:
		return
	# N번째까지 못돌았을 경우
	else:
		
		# Q1이 비어있을 경우 
		if not Q1:
			# Q1 자리에 x,y 좌표를를 넣는다. O(N)
			for i in range(N): 
				dfs(x+1, [x,i], [])
			
			# Q1을 비어있는 상태에서 다음 dfs(x+1)로 돌린다.
			dfs(x+1, [], [])
			
		# Q1이 비어있지 않은경우 Q2랑 비교
		else:
			
			# Q2에 들어갈 x,y 좌표를 모두 체크한다. O(N)
			for i in range(N):
				if check(Q1, [x,i]):
					#print(Q1, [x,i])
					count+=1
			dfs(x+1, Q1, [])

# 따라서 dfs() 함수는 함수내부에서 N^2를 돌기때문에, O(N^2) 평균 시간복잡도를 갖는다. 
N = int(input())
board = [ [0]* N for _ in range(N) ]
#print(board)
count = 0
dfs(0, [], [])
print(count)