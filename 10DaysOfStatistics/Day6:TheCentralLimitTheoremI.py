import math

def cdf(x,mu,sigma): 
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

print(round(cdf(9800,205*49,15*math.sqrt(49)),4))
