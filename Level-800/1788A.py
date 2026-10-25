t = int(input())
for i in range(t):
    n = int(input())
    array = list((int, input().split()))
    if set(array) in [1] or set(array) in [2]:
        print(1)
    else:
        _2 = []
        _1 = []
        operations = 0
        for k in array:
            if k == 2:
                _2.append(k)
            else:
                _1.append(k)
        if len(_2) != len(_1):
            print(-1)
        else:
