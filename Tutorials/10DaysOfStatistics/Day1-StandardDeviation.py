import statistics
n = int(input())
X = [int(i) for i in input().split()]
print(round(statistics.pstdev(X),1))
