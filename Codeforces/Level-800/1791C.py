t = int(input())
for i in range(t):
    n = int(input())
    array = input()
    shortest_length = len(array)
    left_end = array[0]
    right_end = array[-1]
    if left_end == right_end:
        print(shortest_length)
    else:
        i, j = 0, -1
        while (left_end == '1' and right_end == '0') or (left_end == '0' and right_end == '1'):
            shortest_length -= 2
            left_end = array[i+1]
            right_end = array[j-1]
            i += 1
            j -= 1
            if shortest_length == 0:
                break
        print(shortest_length)
