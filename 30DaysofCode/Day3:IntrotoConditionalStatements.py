n=int(input().strip())
#    If is odd, print Weird
if n%2==1:print("Weird")
#    If is even and in the inclusive range of 2 to 5 , print Not Weird
elif n>1 and n<6:print("Not Weird")
#    If is even and in the inclusive range of 6 to 20 , print Weird
elif n>5 and n<21:print("Weird")
#    If is even and greater than 20 , print Not Weird
else:print("Not Weird")