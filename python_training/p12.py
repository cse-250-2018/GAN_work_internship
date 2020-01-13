#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:09:46 2019

@author: sarfaraz
"""

class A:
    def __init__(self):
        #print("object of class A is created")
        pass
    def info(self):
        print("object of class A is created")
class B(A):
    def __init__(self):
        #print("object of class B is created")
        pass
    def info(self):
        print("object of class B  is created")
class C( B, A):
    def __init__(self):
        #print("object of class c is created ")
        pass        
    def info(self):
        print("object of class c is created")
        
a = A();
b  = B();
c = C();

a.info();
b.info();