#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:01:41 2019

@author: sarfaraz
"""

def rando(n):
    a = 1*n;
    b = 2*n;
    c = 3*n;
    return (a,b,c)



_ , _, _= rando(3)


print(_, _,_, sep = '---')