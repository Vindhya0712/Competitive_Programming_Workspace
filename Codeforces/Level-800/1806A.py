t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    operations = 0
    hz_move = 0
    vt_move = 0
    if (d < b):
        print(-1)
    else:
        if (a==c) and (b==d):
            print(operations)
        else:
            vt_move = d-b
            a += vt_move
            if a-c >= 0:
                hz_move = a-c
                operations = hz_move + vt_move
                print(operations)
            else:
                print(-1)
            