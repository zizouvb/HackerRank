da,ma,ya = [int(i) for i in input().split()]
de,me,ye = [int(i) for i in input().split()]
if ya>ye:
    print(10000)
elif ya==ye and ma>me:
    print(500*(ma-me))
elif ya == ye and me == ma and da>de:
    print(15*(da-de))
else: 
    print(0)
