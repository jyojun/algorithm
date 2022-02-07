def solution(s):
    answer = 1001
    reduced_lengths = list()
    if len(s) == 1:
        answer = 1
        return answer 
    for i in range(1,len(s)): # 1개씩~N개씩
        #print(i, "개 단위")
        before_temp = s[0:i]
        reduced_s = str()
        count = 1
        for j in range(i, len(s), i): # index 0부터 i씩 증가
            if j+i > len(s)-1:
                temp = s[j:]
            else:
                temp = s[j:j+i]
            #print(temp)
            if before_temp == temp: 
                count+=1
                #print(before_temp, temp, count)
                before_temp = temp 
            else:
                if count == 1:
                    reduced_s += before_temp
                else:
                    reduced_s += str(count) + before_temp
                    count = 1
                before_temp = temp
        #print('현재 j', j)
        if count > 1: # 마지막까지 같다면 남는 count>1 일 때 더해줌
            reduced_s += str(count) + before_temp
        else:
            reduced_s += temp
        print((reduced_s))
        answer = min(answer, len(reduced_s))
            
    return answer