from collections import Counter
def ransom_note(magazine, ransom):
    return ransom - magazine == {}

m, n = map(int, input().strip().split(' '))
magazine = Counter(input().strip().split(' '))
ransom = Counter(input().strip().split(' '))
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
