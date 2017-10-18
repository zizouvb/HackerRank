
#!/usr/bin/python
import sys
def displayPathtoPrincess(n,grid):
    
    for i in range(len(grid)):
        if 'p' in grid[i]:
            pcol = grid[i].index('p')
            prow = i
        if 'm' in grid[i]:
            mcol = grid[i].index('m')
            mrow = i
    print(pcol, prow,mcol, mrow, file=sys.stderr)
    for i in range(prow-mrow):print("DOWN")
    for i in range(mrow-prow):print("UP")
    for i in range(mcol-pcol):print("LEFT")
    for i in range(pcol-mcol):print("RIGHT")
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

