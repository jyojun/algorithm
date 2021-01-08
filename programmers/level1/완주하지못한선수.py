def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    #print(participant)
    #print(completion)
    if participant[0] != completion[0]:
        return participant[0]
    for i in range(len(participant)):
        if i == len(participant)-1:
            return participant[i]
        else:
            if participant[i] != completion[i]:
                return participant[i]