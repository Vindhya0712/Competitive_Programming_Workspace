t = int(input())
for i in range(t):
    n = int(input())
    string = input()
    souv = []
    kalam = []
    for j in range(len(string)):
        if string[j] == '1':
            souv.append(j+1)
        else:
            kalam.append(j+1)
    if len(souv) >= 3:
        score = max(souv) - min(souv)
    elif len(souv) == 2:
        score = 1
    else:
        score = 0
    print(score)