# Enter your code here. Read input from STDIN. Print output to STDOUT
t1,t2,n = [int(i) for i in input().split()]
if n==0:print(t1)
elif n==1:print(t2)
else:
    for i in range(n-2):
        t3 = t1+t2**2
        t1=t2
        t2=t3
    print(t3)
