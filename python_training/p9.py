#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:21:22 2019

@author: sarfaraz
"""

import numpy as np

x = [1,2, 3, 4,5, 6, 7, 9,10]

np_x = np.array(x)

high = np_x > 2

print(high)

print(np_x[high])

