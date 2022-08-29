def solution(s, n):
    answer = ""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(s)
    temp = s.upper()
    print(temp)
    for i in range(len(temp)):
        if temp[i] == ' ':
            answer += temp[i]
            continue
        if s[i].isupper():
            loc = alphabet.index(s[i])
            loc += n
            loc %= len(alphabet)
            answer += alphabet[loc]
        else:
            loc = alphabet.index(temp[i])
            loc += n
            loc %= len(alphabet)
            answer += alphabet[loc].lower()
    return answer
