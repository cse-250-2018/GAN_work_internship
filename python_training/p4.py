#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:05:59 2019

@author: sarfaraz
"""

def update(x):
    print(id(x))
    
    x = x.append("hello ")
    
    print(id(x))
    print(x)
    
    
a = [1, 2, 3, 4, 5]
print(id(a))
update(a)

print(id(a))
print("a ",a)