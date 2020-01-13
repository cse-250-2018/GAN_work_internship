#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 01:17:59 2020

@author: sarfaraz
"""

import numpy as np

a = np.load('dataset/ds.npy')
b = np.load('dataset/gt.npy')


print(type(a), a.shape, "\n", a);
print("\n")
print(type(b), "\n", b);