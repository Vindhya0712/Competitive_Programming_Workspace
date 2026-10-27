t = int(input())
for i in range(t):
    x, k = map(int, input().split())
    array = []
    if x < k:
        array.append(x)
        print(len(array))
        print(*array)
    else:
        if x % k != 0:
            array.append(x)
            print(len(array))
            print(*array)
        else:
            max_jump = 0
            for j in range(x):
                if j % k != 0:
                    max_jump = j
            if x - max_jump > 0:
                array.extend([max_jump, (x-max_jump)])
            print(len(array))
            print(*array)