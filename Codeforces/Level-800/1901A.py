t = int(input())
for j in range(t):
    n, x = map(int, input().split())
    stations = [int(x) for x in input().split()]
    max_dist = stations[0]
    for i in range(1, n):
        current_dist = stations[i] - stations[i-1]
        max_dist = max(current_dist, max_dist)
    last_leg = (x - stations[n-1]) * 2
    fuel = max(last_leg, max_dist)
    print(fuel)

#So what was the core idea of the question? Well, you need to note the fact that the last leg between the last fuel station
#and the destination is like a min value of the fuel...you need to account for the fact that you need to make the round
#trip, cuz there's no refuel option at the destination...so calculate the round trip distance and store it somewhere...
# let it be a benchmark for the fuel required. Next step, was to find the largest distance between the fuel
#stations and/or the start and end points. Compare this max distance with the benchmark set by the round trip requirement
#The larger value demands the fuel to have that much capacity