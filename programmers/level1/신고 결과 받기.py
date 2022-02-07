def solution(id_list, report, k):
    answer = {}
    call_count = {}
    for i in id_list:
        call_count[i] = list()
        answer[i] = 0
    
    report = list(set(report)) # 중복 제거
    
    for i in report:
        a,b = i.split()
        call_count[b].append(a)
        
    for i in range(len(call_count)):
        if len(call_count[id_list[i]]) >= k:
            for j in call_count[id_list[i]]:
                answer[j] += 1
    result = []
    for i in answer:
        result.append(answer[i])
    return result