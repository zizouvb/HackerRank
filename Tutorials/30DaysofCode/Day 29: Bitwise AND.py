#!/bin/python3

import sys
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    if ((k-1)|k) <= n:print(k-1)
    else: print(k-2)
    
