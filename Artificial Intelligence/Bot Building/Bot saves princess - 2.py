#
def nextMove(n,r,c,grid):
    for i in range(len(grid)):
        if 'p' in grid[i]:
            pcol = grid[i].index('p')
            prow = i
    if pcol-c>0:nextmove = "RIGHT"
    elif prow-r>0:nextmove = "DOWN"
    elif prow-r<0:nextmove = "UP"
    else:nextmove = "LEFT"
    return nextmove
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
