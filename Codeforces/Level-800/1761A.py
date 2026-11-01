t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    if a == b and b == n:
        print("YES")
    elif a+b+2 <= n:
        print("YES")
    else:
        print("NO")
