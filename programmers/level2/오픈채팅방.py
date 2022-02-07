def solution(record):
    answer = []
    user = {}
    for a in record:
        command = a.split()
        if command[0] == 'Enter':
            user[command[1]] = command[2]
        elif command[0] == 'Change':
            user[command[1]] = command[2]
    for a in record:
        command = a.split()
        if command[0] == 'Enter':
            answer.append(f'{user[command[1]]}님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(f'{user[command[1]]}님이 나갔습니다.')

    return answer