import sys
phonebook = {}
for _ in range(int(input())):
    name,number = input().split()
    phonebook[name]=int(number)

queries = map(lambda x: x.strip(),sys.stdin.readlines())

for name in queries:
    if name in phonebook:
        print('{}={}'.format(name, phonebook[name]))
    else:
        print('Not found')
