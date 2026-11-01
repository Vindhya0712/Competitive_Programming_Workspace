import math

t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    flag = 0
    for k in range(n):
        for j in range(k+1, n):
            gcd = math.gcd(array[k], array[j])
            if gcd <= 2:
                flag = 1
                break
    print("YES" if flag == 1 else "NO")
