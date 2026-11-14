t = int(input())
for i in range(t):
    array = list(map(int, input().split()))
    if len(set(array)) == 3:
        if array[0]-array[1] in [1, -1] and array[1]-array[2] in [1, -1]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
