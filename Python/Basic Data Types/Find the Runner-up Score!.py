n = int(input())
arr = set(map(int, input().split()))
arr2 = filter(lambda x:x!= max(arr),arr)
print(max(arr2))
    
