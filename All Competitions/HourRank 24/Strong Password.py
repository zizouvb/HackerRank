#!/bin/python3

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    n=l=s=u=False
    
    for i in password:
        if i in numbers:
            n=True
        if i in lower_case:
            l=True
        if i in upper_case:
            u=True
        if i in special_characters:
            s=True
    strong=4
    if n==True:strong-=1
    if l==True:strong-=1
    if u==True:strong-=1
    if s==True:strong-=1
    answer = strong
    if len(password)<6:
        answer = 6-len(password)
        if strong>answer:
            answer=strong
    return answer


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
