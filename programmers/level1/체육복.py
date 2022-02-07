def solution(n, lost, reserve):
    answer = 0 
    # 여벌을 갖고 온 학생도 도난당한 경우 
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)

    lost_p = list(set_lost)
    for l in lost_p:
        if l-1 in set_reserve:
            set_reserve.remove(l-1)
            set_lost.remove(l)
        elif l+1 in set_reserve:
            set_reserve.remove(l+1)
            set_lost.remove(l)
    answer = n - len(set_lost)
    return answer