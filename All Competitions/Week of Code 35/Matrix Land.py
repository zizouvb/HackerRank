#!/bin/python3

import sys
from itertools import accumulate
def max_at_pos(cum_sum, i):
	maximum = -100000
	for j in range(0,i+1):
		for k in range(i,len(cum_sum)):
		    current_diff = cum_sum[k]-cum_sum[j]
		    if current_diff>maximum:
		        maximum = current_diff			
	
	return maximum
def matrixLand(A):
    # Complete this function
    print(A)
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = []
    B = []
    for A_i in range(n):
        print(A_i)
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        print(A_t)
        cum_sum = list(accumulate(A_t))
        print(cum_sum)
        B_t = [0]*m
        
        for i in range(m):
            B_t[i] = max_at_pos(cum_sum,i)+1
        print(B_t)
        A.append(A_t)
        B.append(B_t)
    
    result = matrixLand(A)
    print(result)
