import sys


n,k = input().strip().split(' ')
n,portee = [int(n),int(k)]
maisons = sorted([int(x_temp) for x_temp in input().strip().split(' ')])


nb_transmitters = 0
i = 0
while i < n:
    nb_transmitters+=1
    
    current_transmitter = maisons[i] + portee
    while i < n and maisons[i] <= current_transmitter: i+=1
    i-=1
    
    current_transmitter = maisons[i] + portee
    while i < n and maisons[i] <= current_transmitter: i+=1
    
print(nb_transmitters);
