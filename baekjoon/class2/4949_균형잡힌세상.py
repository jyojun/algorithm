import sys
input = sys.stdin.readline

while True:
    words = input()
    words = words[:-1] # 마지막 공백문자 때문에 마지막 글자를 지워주고  시작
    result = True
    if words[0]=='.' and len(words)==1:
        break
    else:
        stack = [] # 빈 스택 생성
        words = words.replace(" ", "") # 공백모두 제거
        #print(words)
        for i in range(len(words)):
            #print(stack)
            if words[i] == '(' or words[i] =='[':
                stack.append(words[i])
            elif words[i] == ')' or words[i] ==']':
                if len(stack) == 0: # 오른쪽 괄호가 나왔는데, 빈 스택이라면
                    result = False
                    break
                element = stack.pop()

                if element == '(' and words[i] == ')':
                    continue
                elif element == '[' and words[i] == ']':
                    continue
                else:
                    result = False
                    break
            else:
                continue
        if result and len(stack)==0: #문자열이 끝나고 빈 스택인지도 확인
            print("yes")
        else:
            print("no")