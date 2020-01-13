#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:42:57 2019

@author: sarfaraz
"""

s1 = {1, 3, 4,5}

s1 = set([1,3,5, 6])


print(type(s1))


f1 = frozenset(s1)
print(type(f1))



s1 = {1, 2, 3,"Monday"};
s2 = {"Monday", "Tuesday", "Thursday"}


print(s1|s2)
print(s1.union(s2))


print(s1&s2)
print(s1.intersection(s2))


s3 = {"Monday", "Tuesday", "Wednesday", "Thursday"}

s3.intersection_update(s2,s1)

print(s3)


