# t = int(input())
# for i in range(t):
#     n, m = list(map(int, input().split()))
#     x = input()
#     s = input()
#     counter = 0
#     if s in x:
#         print('0')
#     else:
#         while len(x) < 2*m:
#             x += x
#             counter += 1
#             if s in x:
#                 print(counter)
#                 break
#             else:
#                 continue
#         if len(x) > m and s not in x:
#             print('-1')

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    counter = 0

    while len(x) < m:
        x += x
        counter += 1

    if s in x:
        print(counter)
    else:
        x += x
        counter += 1

        if s in x:
            print(counter)
        else:
            print(-1)