#!/bin/python3

import sys

def lonely_integer(a):
    for i in range(len(a)):
        if a[i] not in a[:i]+a[i+1:]:
            return a[i]

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

