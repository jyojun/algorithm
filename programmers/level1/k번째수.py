def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command[0], command[1], command[2]
        sorted_array = sorted(array[i-1:j])
        answer.append(sorted_array[k-1])
    return answer