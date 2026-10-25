t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort(reverse=True)
    max_value = array[0]
    c = [max_value]
    b = []
    for k in array[1:]:
        if k == max_value:
            c.append(k)
    for j in array:
        if j not in c:
            b.append(j)
    if len(b) == 0:
        print(-1)
    else:
        print(f"{len(b)} {len(c)}")
        print(*b)
        print(*c)