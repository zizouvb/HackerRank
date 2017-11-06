n,m = input().split()
array = [int(i) for i in input().split()]
A = set([int(i) for i in input().split()])
B = set([int(i) for i in input().split()])
print(sum([((i in A) - (i in B)) for i in array]))
