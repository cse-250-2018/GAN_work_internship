#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:56:23 2019

@author: sarfaraz
"""

from pathlib import Path

data_folder = Path("/home/sarfaraz/Desktop/")

file_to_open = data_folder / "commands.txt"

fileptr = open(file_to_open,"r")

if fileptr:
    print("file open success")
else :
    print("file oopen failed")

for i in fileptr:
    print(i)
data = fileptr.readline();
print(data)

data = fileptr.readline();
print(data)

data = fileptr.read();


print(type(data))

print(data)

fileptr.close()


