n, m = map(int,input().strip().split())
count_table = [0]*m
for _ in range(n):
    id_number, amount = map(int,input().strip().split())
    count_table[id_number-1]+= amount    
total_depense = sum(count_table)
count_table[0]-= (total_depense % m)
rest_of_all = total_depense // m

for i in range(m):
    print(i+1 ,count_table[i]-rest_of_all)
