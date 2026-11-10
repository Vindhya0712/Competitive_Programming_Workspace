array = list(map(int, input().split()))
g = array[0]
c = array[1]
l = array[2]
if max(g-c, c-g) >= 10 or max(c-l, l-c) >= 10 or max(l-g, g-l) >= 10:
    print("check again")
else:
    array = sorted(array)
    print(f"final {array[1]}")
