def solution(N, stages):
    
    clear_people = len(stages) # 플레이어 전체 수
    
    all_stages = { x: 0 for x in range(N+2) }
    
    fail_rate = []
    
    for i in range(1, N+1):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] == i: # 도달했으나 못깬사람
                cnt += 1
        if cnt == 0:
            fail_rate.append([0, i])
        else:
            fail_rate.append([cnt/clear_people, i])
        clear_people -= cnt
    fail_rate = sorted(fail_rate, key = lambda x: (-x[0], x[1]))
    
    answer = []
    
    for i in fail_rate:
        answer.append(i[1])
    
    return answer