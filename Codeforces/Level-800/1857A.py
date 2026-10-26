t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if len(array) == 2:
        if array[0] % 2 != array[1] % 2:
            print("NO")
        else:
            print("YES")
    else:
        odd = []
        even = []
        for k in array:
            if k % 2 == 0:
                even.append(k)
            else:
                odd.append(k)
        if len(odd) % 2 == 0:
            print("YES")
        else:
            print("NO")