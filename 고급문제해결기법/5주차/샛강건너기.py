import sys

input = sys.stdin.readline

L, n, k = map(int, input().split())
S = list(map(int, input().split()))

S.append(L)

left, right = 0, L
answer = 0
while left<=right: # O(log2의L)
	expected = (left+right)//2 # 중간을 답이라고 가정.
	#print(expected)
	min_jump = 1000000001 # 필요한 최소 점프값 
	current, cnt = 0, 0 # current : 가장 마지막에 둔 돌. 처음엔 0, cnt : 빼준 돌의 갯수
	for s in S: # 징검다리를 하나씩 살펴본다. 징검다리의 갯수만큼 반복하므로 O(n) 을 갖는다. 
		if s-current < expected: # 기댓답보다 작다면 돌을 뺀다 
			cnt += 1 # 뺀 돌의 갯수를 증가시킴
		else: # 기댓값보다 크거나 같다면 빼지않음.
			min_jump = min(min_jump, s-current) # 필요한 최소 점프값을 업데이트해줌.
			current = s # 현재 돌은 그대로 두기때문에 current값에 현재 탐색중인 돌을 저장 
	
	if cnt > k: # 너무 많이 빼서 좀 덜 빼게 한다. (기대값을 줄임 -> 왼쪽을 살펴봄)
		right = expected-1
	else: # 적게 뺐거나 딱 맞게 뺀 경우 (기대값을 높여본다-> 오른쪽을 살펴봄)
		left = expected+1
		answer = min_jump # 조건에 맞기때문에 일단 점프값을 저장.
		#print(expected, answer)

print(answer)

'''
이 문제의 주요 알고리즘은 이진탐색이다.
L의 최대 크기는 10억이므로 소요시간이 많이 커질 수 있기때문에 고려한 방법이다. 
돌을 최대 개수 k보다 더 뺐을 경우, 점프값의 기대값을 줄이기 위해 더 작은 값의 왼쪽을 탐색한다.
돌이 최대 개수 k보다 덜 뺐거나 딱맞게 뺐을 경우, 우리가 구해야할 값은 최대 k만큼 뺐을때의 점프값의 최대 값이므로
반대로 점프값의 기대값을 높여서 오른쪽을 탐색한다.

while 반복문에서 기본적으로 L크기의 이진탐색을 하므로 O(log2의(L)) 그리고 반복 할 떄마다 징검다리 갯수만큼 
탐색하면서 반복하기 때문에 O(n)을 곱해줘야 한다. 

따라서 총 시간복잡도는 O(n*log2의(L))이다.
'''