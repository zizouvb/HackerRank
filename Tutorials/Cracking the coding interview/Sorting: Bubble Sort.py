n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
nbSwapsTot = 0
for _ in range(n):
    nbSwaps = 0
    for j in range(n-1):
        if a[j]>a[j+1]: 
            a[j+1],a[j] = a[j],a[j+1]
            nbSwaps += 1
            nbSwapsTot += 1
        
    
print("Array is sorted in "+ str(nbSwapsTot) +" swaps.")
print("First Element: "+ str(a[0]) )
print("Last Element: "+ str(a[-1]))
