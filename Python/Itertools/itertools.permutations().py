from itertools import permutations
S,k = input().split()
for l in permutations(sorted(S),int(k)):
    print("".join(l))
