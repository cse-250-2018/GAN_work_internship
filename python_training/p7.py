#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:53:08 2019

@author: sarfaraz
"""

def table(n):
    return lambda a: a*n

n = int(input("enter value of n"))

b = table(n)
for i in range(1,11):
    print(n, " * ", i, " : ", b(i) )
    
