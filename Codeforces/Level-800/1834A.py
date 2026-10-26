t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    s = sum(array)
    operations = 0
    neg = array.count(-1)
    if s >= 0 and (neg % 2 == 0):
        print(0)
    else:
        while (s < 0) or (neg % 2 != 0):
            s += 2
            neg -= 1
            operations += 1
        print(operations)

