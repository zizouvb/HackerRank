# Numpy cannot not be used
# import numpy as np 
N = int(input())
X = [int(integer) for integer in input().split()]
W = [int(weight) for weight in input().split()]
ans = sum([xi*wi for xi,wi in zip(X,W)])/sum(W)
print(round(ans,1))
