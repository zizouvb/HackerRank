x = [95,85,80,70,60]
y = [85,95,70,65,70]

n = len(x)
sumxy = sum([i*j for i,j in zip(x,y)])
sumx2 = sum([i*i for i in x])
b = (n * sumxy - sum(x) * sum(y)) / (n * sumx2 - sum(x)**2)
a = sum(y)/n-b*sum(x)/n

print(round(b*80+a,3))
