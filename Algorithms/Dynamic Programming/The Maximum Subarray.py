# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    length = int(input())
    array = [int(i) for i in input().split()]
    subarray = [i for i in array if i>0]
    if not subarray:
        arr_max=max(array)
    else:
        arr_max=sum(subarray)
    
    max_at_pos = seq_max = array[0]
    for i in range(1,length):
        max_at_pos = max(array[i],max_at_pos+array[i])
        seq_max = max(max_at_pos,seq_max)
    print(seq_max,arr_max)
