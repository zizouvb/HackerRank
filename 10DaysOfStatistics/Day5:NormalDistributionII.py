import math

def cdf(x,mu,sigma): 
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

print(round((1-cdf(80,70,10))*100,2))
print(round((1-cdf(60,70,10))*100,2))
print(round(cdf(60,70,10)*100,2))
