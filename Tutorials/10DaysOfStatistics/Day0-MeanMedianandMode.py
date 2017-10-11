import numpy as np
from collections import Counter
import sys
N = int(input())
X = np.array([int(integer) for integer in input().split()])
print(np.mean(X))
print(np.median(X))
Xfreq = Counter(X)
ans = sys.maxsize
current_max = 0
for i in Xfreq:
    if Xfreq[i]>current_max or (Xfreq[i] == current_max and i<ans):
        ans = i
        current_max = Xfreq[i]
print(ans)       
#print(Xfreq.most_common(1)) 
