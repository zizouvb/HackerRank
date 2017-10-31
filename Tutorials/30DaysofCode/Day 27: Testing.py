import random
t=5
print('{}'.format(t))
for i in range(5):
    n = random.choice(range(3,201))
    k = random.choice(range(1,n+1))
    A = [str(random.choice(range(-10**3,10**3))) for _ in range(n)]
    if 0 not in A:
        A[0]=str(0)
    if all(int(a) >= 0 for a in A):
        A[1]=str(random.choice(range(-10**3,0)))
    if all(int(a) <= 0 for a in A):
        A[2]=str(random.choice(range(10**3)))
    print('{} {}'.format(n,k))
    print(' '.join(A))