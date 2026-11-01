t = int(input())
for i in range(t):
    n = int(input())
    string = input()
    operations = 0
    if "..." in string:
        operations = string.count("...") * 2
    else:
        operations += string.count('.')
    print(operations)