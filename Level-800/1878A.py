t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    if k in array:
        print("YES")
    else:
        print("NO")

#The key idea was the fact that the most common element did not have a constraint saying that the subarray had to have a
#min length greater than 1....so you can literally pick the element itself and call it a subarray and say that it's the
#mode in the subarray...so it all comes down to checking if k exists in the given array