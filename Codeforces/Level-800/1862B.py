t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    answer = [array[0]]
    if len(answer) <= 2*n:
        for k in range(1, n):
            if array[k-1] > array[k]:
                answer.append(array[k])
                answer.append(array[k])
            else:
                answer.append(array[k])
    print(len(answer))
    print(*answer)