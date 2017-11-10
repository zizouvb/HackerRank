for _ in range(int(input())):
    _ = input()
    a = sorted([int(i) for i in input().split()])
    ans0 = ans1 = ans2 = 0 
    nb_op = [0,1,1,2,2,1]
    for i in a:
       
        ans0 += nb_op[(i-a[0])%5] + (i-a[0])//5
        ans1 += nb_op[(i-(a[0]-1))%5] + (i-(a[0]-1))//5
        ans2 += nb_op[(i-(a[0]-2))%5] + (i-(a[0]-2))//5
       
    print(min(ans0,ans1,ans2))
