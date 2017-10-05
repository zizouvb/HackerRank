from math import erf, sqrt

#F(19.5)
print(round(1/2-1/2*erf(1/sqrt(2)*1/4),3))
#F(22)-F(20)
print(round(1/2+1/2*erf(1/sqrt(2))-1/2,3))
