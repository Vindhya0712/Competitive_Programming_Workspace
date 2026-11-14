t = int(input())
for i in range(t):
    n = int(input())
    string = input().upper()
    current = 'R'
    counter = 0
    for char in string:
        if char != current:
            current = char
            counter += 1
        if current == 'R':
            current = 'B'
        else:
            current = 'R'
    print(counter)