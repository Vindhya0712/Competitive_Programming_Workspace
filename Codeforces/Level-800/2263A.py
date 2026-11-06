t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if array.count(1) >= array.count(0):
        print("Bessie")
    else:
        print("Elsie")