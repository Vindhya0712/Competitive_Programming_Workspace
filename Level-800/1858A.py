t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if c % 2 != 0:
        if (a + (c % 2 + 1)) > (b + (c % 2)):
            print("First")
        else:
            print("Second")
    if c % 2 == 0:
        if a > b:
            print("First")
        else:
            print("Second")
