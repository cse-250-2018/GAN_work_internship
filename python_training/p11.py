#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:59:19 2019

@author: sarfaraz
"""

class employee:
    def __init__(self, id1, name):
        self.id1 = id1
        self.name = name
    
    def display(self):
        print(self.id1, self.name)
        
        
obj = employee(17103078, "Sarfaraz");
obj.display()