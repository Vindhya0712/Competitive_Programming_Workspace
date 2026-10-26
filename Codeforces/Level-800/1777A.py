t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    operations = 0
    for k in range(len(array)-1):
        if array[k] % 2 == array[k+1] % 2:
            operations += 1
    print(operations)