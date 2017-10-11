# def number_needed(a, b):
#     count = 0
#     for i in range(97, 123):
#         ia = sum(letter == chr(i) for letter in a)
#         ib = sum(letter == chr(i) for letter in b)
#         count += abs(ia-ib)
#     return count

def number_needed(a, b):
    nb_to_delete = 0
    for _ in range(len(a)):
        letter=a[0]
  
        if letter in b:
  
            b.remove(letter)
        else:
  
            nb_to_delete+=1
        a.remove(letter)
  
    return nb_to_delete + len(b)

a = list(input().strip())
b = list(input().strip())

print(number_needed(a, b))
