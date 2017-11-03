def getRecord(s):
    # Complete this function
    down = up = s[0]
    nb_d = nb_u = 0
    for g in s[1:]:
        if g>up:
            nb_u+=1
            up=g
        if g<down:
            nb_d+=1
            down=g
    return nb_u,nb_d
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
