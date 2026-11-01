t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    round_numbers = []
    for multiplier in range(7):
        for digit in range(1, 10):
            round_numbers.append(digit * (10**multiplier))
    for k in round_numbers:
        if k <= n:
            count += 1
    print(count)