t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    operations = 0
    if array != sorted(array):
        print(0)
    elif array == sorted(array):
        diff_array = []
        for k in range(len(array) - 1):
            diff_array.append(array[k+1] - array[k])
        min_diff = min(diff_array)
        operations = min_diff // 2 + 1
        print(operations)