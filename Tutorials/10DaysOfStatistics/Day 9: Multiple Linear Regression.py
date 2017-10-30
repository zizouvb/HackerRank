import numpy as np
from sklearn import linear_model
m,n = [int(i) for i in input().split(' ')]
X = np.zeros((n,m))
Y = np.zeros(n)
for i in range(n):
    data = input().split(' ')
    X[i,:]=data[:m]
    Y[i]=data[-1]
lm = linear_model.LinearRegression()
lm.fit(X, Y)
q = int(input().strip())
for i in range(q):
    X_test=[float(j) for j in input().split(' ')]
    print(round(float(lm.predict(X_test)),2))
