t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    S = sum(array)
    print(-S)
