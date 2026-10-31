t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if array == sorted(array):
        print("YES")
    elif (array[0] != min(array)):
        print("NO")
    else:
        print("YES")

