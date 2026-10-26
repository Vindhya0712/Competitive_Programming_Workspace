t = int(input())
for i in range(t):
    array = list(map(int, input().split()))
    n = array[0]
    k = array[1]
    x = array[2]
    answer = []
    if k == 1 and x == 1:
        print("NO")
    elif k == 2 and x == 1:
        if n % 2 != 0:
            print("NO")
        else:
            for j in range(n//2):
                answer.append(2)
            print(f"YES \n{len(answer)}")
            print(*answer)
    elif x != 1:
        for j in range(n):
            answer.append(1)
        print(f"YES \n{len(answer)}")
        print(*answer)
    elif x == 1 and k >= 3:
        if n % 2 == 0:
            for j in range(n//2):
                answer.append(2)
            print(f"YES \n{len(answer)}")
            print(*answer)
        else:
            answer.append(3)
            n -= 3
            for j in range(n//2):
                answer.append(2)
            print(f"YES \n{len(answer)}")
            print(*answer)
    elif n == 1 and x == 1:
        print("NO")