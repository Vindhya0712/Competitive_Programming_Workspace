import random

t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    answer = []
    while len(answer) >= n and len(answer) <= 2*n:
        answer.append(array[0])
        for k in 
    print(len(answer))
    print(*answer)