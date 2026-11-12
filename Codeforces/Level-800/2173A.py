t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    array = input()
    counter = 0
    answer = 0
    for char in array:
        if char == '1':
            counter = k
        elif counter > 0:
            counter -= 1
        else:
            answer += 1
    print(answer)

#     if '1' not in array:
#         print(n)
#     elif '0' not in array:
#         print(0)
#     else:
#         for j in range(k, -1, -1):
#             string_to_check = '1' + '0' * j
#             if string_to_check in array:
#                 array = array.replace(string_to_check, "", 1)
#         print(len(array))
# the problem with my approach is that I am removing the string, constantly changing it, which causes unexpected outputs
# instead of that, I should prolly keep a variable as a counter
