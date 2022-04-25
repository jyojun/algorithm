import math

def solution(progresses, speeds):
    answer = []
    total_days = []
    stack = []
    for i in range(len(progresses)):
        stack.append([progresses.pop(), speeds.pop()])
    
    #print(stack)
    
    while stack:
        left_work = 100 - stack[-1][0]
        days = math.ceil(left_work / stack[-1][1])
        total_days.append(days)
        stack.pop()
        
    #print(total_days)
    cnt = 1
    curr_work = total_days[0]
    for i in range(1, len(total_days)):
        if i != len(total_days)-1:
            if curr_work >= total_days[i]:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
                curr_work = total_days[i]
        else:
            if curr_work >= total_days[i]:
                cnt += 1
                answer.append(cnt)
            else:
                answer.append(cnt)
                cnt = 1
                answer.append(cnt)
                
        print(cnt)
        
    return answer