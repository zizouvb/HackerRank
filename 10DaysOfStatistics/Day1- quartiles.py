import statistics
import math
n = int(input())
X = sorted([int(integer) for integer in input().split()])
lower_half = X[:math.floor(n/2)]
upper_half = X[math.ceil(n/2):]
q1 = statistics.median(lower_half)
q2 = statistics.median(X)
q3 = statistics.median(upper_half)

print("{:g}".format(statistics.median(lower_half)))
print("{:g}".format(statistics.median(X)))
print("{:g}".format(statistics.median(upper_half)))
