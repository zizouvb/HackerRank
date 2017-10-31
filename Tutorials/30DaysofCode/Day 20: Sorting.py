import sys
  
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total_nb_swap = 0
for i in range(n):
    current_nb_swap = 0
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            current_nb_swap += 1 
    
    if current_nb_swap==0:
        break
    total_nb_swap += current_nb_swap
print("Array is sorted in {} swaps.".format(total_nb_swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))