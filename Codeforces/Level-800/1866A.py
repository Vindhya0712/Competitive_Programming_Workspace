n = int(input())
array = list(map(int, input().split()))
operations = 0
if 0 not in array:
    mod_array = []
    for i in array:
        if i < 0:
            mod_array.append(-i)
        else:
            mod_array.append(i)
    min_value = min(mod_array)
    operations = max(min_value, -min_value)
    print(operations)
else:
    print(operations)