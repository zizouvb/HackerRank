
t = int(input().strip())
for _ in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    current_max=0
    for a in range(1,n):
        for b in range(a+1,n+1):
            bitwise_and = a&b
            if bitwise_and > current_max and bitwise_and < k:
                current_max = bitwise_and
    print(current_max)     