#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:50:41 2019

@author: sarfaraz
"""
import sys


a = 10;
b = 12;
c = a+b;
print(c)


a , b, c = 5, 10, 15;


a  =b = c = 15;


str = "Sarfraz"

str1 = 'a'

t1 = (17103078, "Sarfraz")
t1[1]

t2 = (17103077, "sankalp")

t3= t2 - t1
print(t3)



l1 = [17103078, "Sarfaraz"]

"Sarfaaz" not in l1
l2 = [17103077, "Sankalp"]


l3 = l2+l1
print(l3)

l3.pop();
print(l3)

l3 = l3 - l1


d = { 17103078: "Sarfaraz", 17103079:"Sarthak"}

print(d)
d.keys();

name = d[17103078];
d[17103078] = "Alam"
print(d)

print(type(d));
print(type(l1));
print(type(name));
print(type(t1));


a3 = 3
print(a3)
name3 = str(sys.maxsize)
print(name3*3)






1!=2



















