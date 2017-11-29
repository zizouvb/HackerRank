def is_matched(expression):
    arr = list()
    for i in expression:
        
        if i=="(" or i=="{" or i=="[":
            arr.insert(0,i)
        else:
            if arr==[]:
                return False
            else:
                j=arr.pop(0)
                if (i=="]" and j!="[") or (i=="}" and j!="{") or (i==")" and j!="("):
                    return False
    if arr!=[]:
        return False
    
    return True
        

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
"""
Tricky solution find on Discussion
def is_matched(e):
    while( len(e) > 0):
        t = e
        e = e.replace('()','')
        e = e.replace('{}','')
        e = e.replace('[]','')
        if t == e:
            return False
        
    return True
"""