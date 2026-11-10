t = int(input())
for i in range(t):
    n = int(input())
    given, target = map(str, input().lower().split())
    given_list = [char for char in given]
    target_list = [char for char in target]
    given_list = sorted(given_list)
    target_list = sorted(target_list)
    print("YES" if given_list == target_list else "NO")

