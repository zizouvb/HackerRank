n = int(input())
X = [float(i) for i in input().split()]
Y = [float(i) for i in input().split()]
indices_x = list(range(len(X)))
indices_y = list(range(len(Y)))
indices_x.sort(key=lambda i:X[i])
indices_y.sort(key=lambda i:Y[i])
rank_x = [0]*n
rank_y = [0]*n
for i,x in enumerate(indices_x):
    rank_x[x]=i
for i,y in enumerate(indices_y):
    rank_y[y]=i
d = [rx - ry for rx,ry in zip(rank_x,rank_y)]
Di = sum([di*di for di in d])
print(round(1-6*Di/(n*(n**2-1)),3))