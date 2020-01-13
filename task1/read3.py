#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 19:52:37 2019

@author: sarfaraz
"""
import matplotlib.pyplot as plt
import numpy as np
import gdal
# Reading Header file
def hdr_read(path):
    row = 0
    col = 0
    bands = 0
    datatype = None
    with open(path, "r") as f:
        for l in f:
            k = l.split()
            if k[0] == "BANDS:":
                bands = k[1]
            elif k[0] == 'ROWS:':
                row = k[1]
            elif k[0] == 'COLS:':
                col = k[1]
            elif k[0] == 'DATATYPE:':
                datatype = k[1]
    mul, D_type = (255, 'uint8') if datatype == 'U8' else ((2**16-1), 'U16')
    row = int(row)
    col = int(col)
    bands = int(bands)
    return row, col, bands, datatype




def ReadBilFile(bil,bands):#,pixels):
    extract_band = 1
    #image = np.zeros([pixels, bands], dtype=np.uint16)
    gdal.GetDriverByName('EHdr').Register()
    bil =str(bil)
    img = gdal.Open(bil)
    
    x = 1
    alist = []
    while bands >= extract_band:
        bandx = img.GetRasterBand(extract_band)
        datax = bandx.ReadAsArray()
        
        temp = datax
        print(type(datax))
        print(datax.shape)
        alist.append(datax)
# =============================================================================
#         store = temp.reshape(pixels)
#         for i in range(pixels):
#             image[i][extract_band - 1] = store[i]
# =============================================================================
        extract_band = extract_band + 1
    return alist


from pathlib import Path
data_folder = Path("/home/sarfaraz/Desktop/isro@internship/GAN Cloud Images-20191215T170608Z-001")

file_to_open = data_folder / "stacked_june_19.hdr"
print(file_to_open)
a = hdr_read(file_to_open)  
print(type(a))
print(a)
print("rows: ",a[0], "\ncolumn : ",a[1], "\nbands : ",a[2], "\ndatatype : ",a[3])
 
file_bil = data_folder / 'stacked_june_19'
pixels = 499
op1 = ReadBilFile(file_bil,a[2])#,  a[1]*a[0])
print(type(op1))
print(op1)
# 
print(type(op1), "\nshape:========== \n")#,op1.shape)
numpy1 = np.dstack(op1)
print(numpy1)
print(type(numpy1),"\n\n",numpy1.shape)


for i in range(0,10):
    print('stack  := ',i,' = ',numpy1[:,:,i])
    

# =============================================================================
# 
# image = np.zeros([pixels, bands], dtype=np.uint16)
# =============================================================================
