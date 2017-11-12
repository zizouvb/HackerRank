def candies(n, arr):
    # Complete this function
    candies_arr = [0]*n
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            candies_arr[i]=candies_arr[i-1]+1

    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1] and candies_arr[i]<=candies_arr[i+1]:
            candies_arr[i]=candies_arr[i+1]+1
     return sum(candies_arr)+n

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = int(input().strip())
        arr.append(arr_t)
    result = candies(n, arr)
    
    print(result)

