n,d = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
print(sum([arr[i]+d in arr[i:] and arr[i]+2*d in arr[i:] for i in range(n-2)]))
 
  
