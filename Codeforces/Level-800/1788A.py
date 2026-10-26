t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    _2 = array.count(2)
    _1 = array.count(1)
    if _1 == len(array):
        print(1)
    else:
        if _2 % 2 != 0:
            print(-1)
        else:
            target = _2//2
            counter = 0
            for index, k in enumerate(array, start=1):
                if k == 2:
                    counter += 1
                if counter == target:
                    print(index)
                    break
