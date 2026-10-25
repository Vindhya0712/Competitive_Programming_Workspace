t = int(input())
for j in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if n == 2:
        print("YES")
        continue
    distinct_elements = list(set(array))
    a = 0
    b = 0
    if len(distinct_elements) == 2:
        for i in array:
            if i == distinct_elements[0]:
                a += 1
            else:
                b += 1
        if a-b in [0, 1] or b-a in [0, 1]:
            print("YES")
        else:
            print("NO")
    elif len(distinct_elements) == 1:
        print("YES")
    else:
        print("NO")