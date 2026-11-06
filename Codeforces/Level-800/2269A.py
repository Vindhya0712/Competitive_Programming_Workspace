t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print((2 ** (n-k+1)) + 2 * (k-1))