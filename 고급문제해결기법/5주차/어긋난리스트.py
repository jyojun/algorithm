import sys

input = sys.stdin.readline

A = list(map(int, input().split()))

result = False # rotation 했는지에 대한 여부 
for i in range(1,len(A)-1): # 리스트의 길이 만큼 반복
	if A[-i-1] > A[-i]: # 뒤에서 부터 탐색할때, 자신의 앞이 자신보다 큰 값이면 출력
		print(i)
		result = True 

if not result: # 마지막까지 없다면 출력하지 않으면 rotation 하지 않은 것이므로 0을 출력
	print(0)
	
# 반복문이 총 리스트의 n번을 돌기 때문에 O(n)의 시간복잡도를 갖는다.