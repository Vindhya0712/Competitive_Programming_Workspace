t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    given_list = [int(x) for x in input().split()]
    if k == 1:
        print("YES" if given_list == sorted(given_list) else "NO")
    else:
        print("YES")
"""sorted() returns a new list that's sorted...sort() sorts the original list and returns None, hence the 3rd test case 
failed initially.
Also, the main logic of the code was basically the fact that if k > 1, you CAN sort the array by just reversing the 
subarrays multiple times. The other piece of the logic was detecting the behaviour when k == 1"""