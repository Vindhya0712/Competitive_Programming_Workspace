t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if b >= a:
        print(-1)
    elif b == 1:
        print(1)
    else:
        print(min(b, a-b))