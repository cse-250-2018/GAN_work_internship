#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:45:20 2019

@author: sarfaraz
"""

def squares(n):
    return n*n

l = [1, 3, 4, 5]

result = map(squares, l)

print(result)

s1 = set(result)


print(s1)

a = zip(l, s1)

a1 = set(a)
print(a1)
print(type(a1))
print(a1)
