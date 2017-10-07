string_occ = {}
for _ in range(int(input())):
    cur_string = input()
    if cur_string in string_occ:
        string_occ[cur_string] += 1
    else:
        string_occ[cur_string] = 1

for _ in range(int(input())):
    cur_string = input()
    if cur_string in string_occ:
        print(string_occ[cur_string])
    else:
        print("0")
