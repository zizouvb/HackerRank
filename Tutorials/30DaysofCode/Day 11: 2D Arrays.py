arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
max_sum = -1000
for i in range(1,5):
    for j in range(1,5):
        cur_sum = sum(arr[j-1][i-1:i+2]) + arr[j][i] + sum(arr[j+1][i-1:i+2])
        
        if cur_sum>max_sum:
            max_sum = cur_sum
            
print(max_sum)
