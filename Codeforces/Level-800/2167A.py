t = int(input())
for i in range(t):
    array = list(map(int, input().split()))
    print("YES" if len(set(array)) == 1 else "NO")