import sys

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a, b, x = input().strip().split(' ')
        a, b, x = [int(a), int(b), int(x)]
        
        if x>(b+1)/2:
            print(-1)
        else:
            for i in range(b-x+1,b+1):
                print(i,end=" ")
            print()    
