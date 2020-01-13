#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:26:32 2019

@author: sarfaraz
"""

 a = int(100)
 b = bin(a)
 print(b)
 
 
 print(bool(b))
 
 test = [0]
 print(bool(test))
 
 
 str = "Sarfaraz"
 
 str1 = bytes(str, 'utf-8')
 
 print(type(str1))
 
 
 s1 = [1, 3, 4,  1]
 print(sum(s1))
 
 
 
 it = iter(s1)

 while it != None:
     print(next(it))
   