import statistics
n = int(input())
X = [float(i) for i in input().split()]
Y = [float(i) for i in input().split()]
mu_x = sum(X)/n
mu_y = sum(Y)/n
sigma_x = statistics.pstdev(X)
sigma_y = statistics.pstdev(Y)
num = sum([(x-mu_x)*(y-mu_y) for x,y in zip(X,Y)])
dem = n * sigma_x * sigma_y
print(round(num/dem,3))
