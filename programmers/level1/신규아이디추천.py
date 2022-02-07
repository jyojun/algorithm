def solution(new_id):
    answer = ''

    # 1. 대문자 -> 소문자
    new_id = new_id.lower()

    # 2. 
    for i in new_id:
        if (not(i >= '0' and i <= '9') and not(i >= 'a' and i <= 'z')) and (not(i >= 'A' and i <= 'Z') and i != '-' and i != '_' and i != '.'):
            new_id = new_id.replace(i, "")
    # 3.
    new_id = new_id.replace('..', '.')
    
    # 4.
    if new_id[len(new_id)-1] == '.':
        new_id = new_id[:len(new_id)-1]
    if new_id[0] == '.':
        new_id = new_id[1:]

    # 5.
    if len(new_id) == 0:
        new_id = 'a'
    
    # 6.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[len(new_id)-1] == '.':
        new_id = new_id[:len(new_id)-1]
    
    # 7.
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1]
    
    answer = new_id
    return answer

print(solution("abcdefghijklmn.p"))