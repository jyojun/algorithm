import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

# 결과를 저장할 n 만큼 크기의 리스트를 생성 
result = [0 for _ in range(n)]


# n명의 시민, n명의 후보 
for i in A:
	result[i] += 1

# 후보가 있는지 없는지 확인하는 변수	
answer = False

# n만큼 투표한 결과에서 하나하나 살펴본다 사람수 N번만큼 살펴보므로, 시간복잡도 O(N) 
for person in result:
	
	# 한 사람이 과반수 이상 받을 경우 인덱스 출력
	if person > n/2:
		print(result.index(person))
		answer = True
	
	# 과반수 이상이 아닐경우 계속 for문을 돈다.
	else:
		continue
# 다 돌때까지 과반수 이상 받은사람이 없을 경우		
if answer == False:
	print(-1)
	
# 총 평균 시간복잡도 O(N)