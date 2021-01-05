words = input()
words = words.strip() #앞뒤 공백 제거

if len(words)==0:
    print(0)
else:
    print(words.count(" ")+1)