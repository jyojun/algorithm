import sys
input = sys.stdin.readline
#'''
n = int(input())
movie = 0
count = 0
while True:
    if '666' in str(movie):
        #print(movie, count, str(movie).count('6'))
        count+=1
    movie+=1
    if count==n:
        break
print(movie-1)
'''

N = int(input())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)
'''