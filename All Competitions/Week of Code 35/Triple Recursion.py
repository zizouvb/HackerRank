import sys

def tripleRecursion(n, m, k):
    # Complete this function
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                a[i][j]=m
            elif i==j:
                a[i][j]=a[i-1][j-1]+k
            elif i>j:
                a[i][j]=a[i-1][j]-1
            else:
                a[i][j]=a[i][j-1]-1
    for i in range(n):
        print(" ".join([str(j) for j in a[i]]))
if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
