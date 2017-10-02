n = 10
p = 0.12
answer1 = (1-p)**10 + 10*(1-p)**9*p + 45*(1-p)**8*p**2
answer2 = (1-p)**10 + 10*(1-p)**9*p 
print("{:.3f}".format(answer1))
print("{:.3f}".format(1-answer2))
