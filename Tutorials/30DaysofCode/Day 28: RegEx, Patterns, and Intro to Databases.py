#!/bin/python3

import sys

db = []
N = int(input().strip())
for i in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    if emailID[-10:]=="@gmail.com":
        db.append(firstName)
db.sort()
for name in db:
    print(name)
