t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    answer = []
    if len(set(array)) == 1:
        print("NO")
    else:
        print("YES")
        array.sort(reverse=True)
        answer.append(array[0])
        array.remove(array[0])
        array.sort()
        answer.extend(array) #append creates a nested list situation....so using extend instead
        print(*answer) #unpacks the list elements and prints in the desired format for this question
