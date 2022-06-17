def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    total_days = 0
    for i in range(a-1):
        total_days += days[i]
    total_days += b

    return day[total_days % 7]

# 0 목 1 금 2 토 3 일 4 월 5 화 6 수
