import math
import statistics
n = int(input())
X = [int(i) for i in input().split()]
F = [int(f) for f in input().split()]
S = list()
for i in range(len(X)):
    S.extend([X[i]]*F[i])
S.sort()

lower_half = S[:math.floor(len(S)/2)]
upper_half = S[math.ceil(len(S)/2):]

print("{0:0.1f}".format(statistics.median(upper_half)-statistics.median(lower_half)))

