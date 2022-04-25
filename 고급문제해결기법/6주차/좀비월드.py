import sys

input = sys.stdin.readline

n, L, k = map(int, input().split())

zombies = [] # 좀비 리스트의 원소 리스트는 [ 좀비위치, 좀비 번호(방향용), 좀비 처음 번호(마지막 출력용) ] 으로 이루어짐 

for i in range(n):
	pos, idx = map(int, input().split())
	zombies.append([pos-(L/2), idx, idx]) #편의를 위해 위치를 -L/2 ~ L/2 까지 라고 생각(나중에 절댓값으로 먼저떨어진 순서를 정하기 위해)
#print(zombies)

cnt = 0
fall_order = []
while cnt < k: # k마리 떨어질 때까지 반복
	time = 0
	min_dis = L
	for i in range(len(zombies)-1):
		if zombies[i][1] > 0 and zombies[i+1][1] < 0: # 서로 바라보고있는 방향 일 때,
			#print("마주보고있음", zombies[i][0], zombies[i+1][0])
			if min_dis > zombies[i+1][0] - zombies[i][0]: # 좀비들 사이의 최소거리를 업데이트
				min_dis = zombies[i+1][0] - zombies[i][0]
		time = min_dis / 2 # 최소거리를 마주보는 좀비 두마리가 만나는데 걸리는 시간

	# 각 좀비를 마주보는 좀비들중 가장 가까운 거리의 좀비들이 만나는 시간만큼 이동시켜줌 O(n)
	for i in range(len(zombies)):
		# 왼쪽으로 이동(왼쪽을 보고있는 좀비) 
		if zombies[i][1] < 0:
			zombies[i][0] -= time
			
		# 오른쪽으로 이동(오른쪽을 보고있는 좀비)
		else:
			zombies[i][0] += time
	
	# 만난(부딪힌) 좀비의 방향을 바꿔줌 O(n)
	for i in range(len(zombies)-1):
		
		if zombies[i][0] == zombies[i+1][0]:
			zombies[i][1], zombies[i+1][1] = -zombies[i][1], -zombies[i+1][1]
			#print(zombies[i][1], zombies[i+1][1], "부딪힘")
	
	# 떨어진 좀비를 리스트에 넣음 O(nk)
	for i in range(len(zombies)):
		# 맨앞과 맨 끝 비교
		if (zombies[i][0] > L/2 or zombies[i][0] < -(L/2)): # 떨어진 좀비중 이미 떨어져서 리스트에 있는 좀비는 또 넣지 않음.
			already = False
			for j in range(len(fall_order)): # fall_order는 최대 k만큼 크기 반복 O(k)
				if fall_order[j][1] == zombies[i][1]:
					already = True
					break
			if not already:
				fall_order.append(zombies[i])
				#print(zombies[i], "떨어짐")
				cnt += 1
#print(fall_order)

# fall_order 에 좀비가 k마리 담길때까지 총 k*(n+n+nk) -> O(2nk+n*k^2) 시간복잡도

# 떨어진 좀비의 위치를 모두 절댓값으로 표기 O(k)
for fall in fall_order:
	fall[0] = abs(fall[0])
	
fall_order.sort() # 정렬 O(klogk)

# 마지막으로 양끝에서 동시에 떨어졌다면 아이디가 더 작은 좀비가 더 빨리 떨어지도록 순서를 변경 O(k)
for i in range(len(fall_order)-1):
	if (fall_order[i][0] == fall_order[i+1][0]) and (fall_order[i][2] < fall_order[i+1][2]):
		fall_order[i], fall_order[i+1] = fall_order[i+1], fall_order[i]

# 오름차순 정렬이므로 위치의 절댓값이 뒤에서 ㅏ 번째로 큰 좀비가 ㅏ번째 떨어진 좀비다 
print(fall_order[-k][2])

# 총 시간 복잡도 k*(n+n+nk)+k+klogk+k => O(2nk+n*k^2+2k+klogk)의 시간복잡도를 갖는다. 
# 최고차항과, 최고차항의 계수를 제외한다면 평균은 O(n*k^2), k = n 일 최악의 상황에서 O(n^3)의 시간복잡도를 갖게된다.  