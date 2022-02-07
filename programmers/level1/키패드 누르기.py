def solution(numbers, hand):
    answer = ''
    left_nums = [1,4,7]
    right_nums = [3,6,9]
    left_loc = '*'
    right_loc = '#'
    keypad = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['*','0','#'],
    ]
    for number in numbers:
        if number in left_nums:
            answer += 'L'
            left_loc = str(number)
        elif number in right_nums:
            answer += 'R'
            right_loc = str(number)
        else:
            for i in range(len(keypad)):
                for j in range(len(keypad[i])):
                    if keypad[i][j] == left_loc:
                        left_dist = i, j
                    if keypad[i][j] == right_loc:
                        right_dist = i, j
                    if keypad[i][j] == str(number):
                        target = i, j 
            #left_dist = keypad.index(left_loc)
            #right_dist = keypad.index(right_loc)
            #target = keypad.index(str(number))
            if abs(left_dist[0] - target[0]) + abs(left_dist[1] - target[1]) < abs(right_dist[0] - target[0]) + abs(right_dist[1] - target[1]):
                answer += 'L'
                left_loc = str(number)
            elif abs(left_dist[0] - target[0]) + abs(left_dist[1] - target[1]) > abs(right_dist[0] - target[0]) + abs(right_dist[1] - target[1]):
                answer += 'R'
                right_loc = str(number)
            else:
                if hand == 'left':
                    answer += 'L'
                    left_loc = str(number)
                else:
                    answer += 'R'
                    right_loc = str(number)
    return answer