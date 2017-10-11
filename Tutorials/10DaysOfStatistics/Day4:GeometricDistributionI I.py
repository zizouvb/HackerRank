p = 1/3
answer = 0
for i in range(5):
    answer += (1-p)**i*p
print(round(answer,3))
