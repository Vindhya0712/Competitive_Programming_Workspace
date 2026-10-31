t = int(input())
for i in range(t):
    n = int(input())
    array = map(int, input().split())
    target = n+1
    b = []
    for k in array:
        b.append(target - k)
    print(*b)