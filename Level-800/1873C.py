t = int(input())
for i in range(t):
    grid = []
    for j in range(10):
        row = input()
        grid.append(row)
    total_score = 0
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 'X':
                ring = min(r, c, 9-r, 9-c)
                points = ring+1
                total_score += points
    print(total_score)
"""See, to find where exactly the X is on the ring...we need to find the minimum value of r, c, 9-r and 9-c.
r -- row, c -- col, 9-r & 9-c -- because python lists are indexed from 0. The min of these 4 values tells us which ring 
the arrow is in. And then you add 1 to get the score for the arrow in that ring, cuz the ring numbers will be 0,1,2,3,4
but the points are 1,2,3,4,5"""