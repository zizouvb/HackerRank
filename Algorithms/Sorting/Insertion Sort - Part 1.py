n = int(input())
ar = [int(i) for i in input().split()]
e = ar[-1]
ar = ar[:-1]
pos = len(ar)
while (ar[pos-1]>e and pos>0):
    print(*map(str,ar[:pos-1]), ar[pos-1], *map(str,ar[pos-1:]))
    pos -= 1
print(*map(str,ar[:pos]), e, *map(str,ar[pos:]))
