#[TO REVIEW] Does not pass all test cases. 

from fractions import gcd

def maximumGcdAndSum(A, B):
    # Complete this function
    maxGcd=0
    max_sum=0
    for a in A:
        for b in B:
            if gcd(a,b)>maxGcd:
                maxGcd=gcd(a,b)
                max_sum = a+b
            elif gcd(a,b)==maxGcd:
                if a+b>max_sum:
                    max_sum=a+b
    return max_sum
if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)
