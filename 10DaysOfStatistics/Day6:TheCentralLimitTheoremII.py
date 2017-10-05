import math

def cdf(x,mu,sigma): 
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

print(round(cdf(250,2.4*100,2*math.sqrt(100)),4))
