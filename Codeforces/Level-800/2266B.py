t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if (a+c) > b:
        if max((a+c) - b, b - (a+c)) >= max(a-b, b-a):
            print(max((a+c) - b, b - (a+c)))
        else:
            print(max(a-b, b-a))
    else:
        print(max(a-b, b-a))