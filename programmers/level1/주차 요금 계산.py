import math 

def solution(fees, records):
    answer = []
    
    cars_records = {}
    
    # 차량별로 기록 
    for record in records:
        time, car_num, action = record.split()
        
        if car_num not in cars_records: 
            cars_records[car_num] = [[time, action]]
        else:
            cars_records[car_num].append([time, action])
    
    for car_num in cars_records:
        if cars_records[car_num][-1][1] != "OUT": # 마지막에 나간게 없는 경우
            cars_records[car_num].append(["23:59", "OUT"])
    
    cars_records
    #print(cars_records)
    
    # 요금 계산 (차량번호 순으로)
    for car_num in sorted(cars_records.keys()):
        sum = 0
        sum_minute = 0
        #print(car_num)
        for i in range(0,len(cars_records[car_num]),2):
            out_hour, out_minute = cars_records[car_num][i+1][0].split(':')
            in_hour, in_minute = cars_records[car_num][i][0].split(':')
            out_hour, out_minute = int(out_hour), int(out_minute)
            in_hour, in_minute = int(in_hour), int(in_minute)
            
            if out_minute < in_minute:
                out_hour -= 1
                out_minute += 60
            
            sum_minute += 60*(out_hour-in_hour) + (out_minute-in_minute)

        sum += fees[1]
        # 기본 시간보다 길 경우
        if sum_minute > fees[0]:
            sum += math.ceil((sum_minute - fees[0])/fees[2])*fees[3]
        #print(car_num, sum)
        answer.append(sum)
    return answer