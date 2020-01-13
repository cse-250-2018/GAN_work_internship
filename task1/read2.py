#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:08:16 2019

@author: sarfaraz
"""

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
            #print(type(k))
            #print('checking k : ')
            #print(k)
            if k[0] == "BANDS:":
                bands = k[1]
            elif k[0] == 'ROWS:':
                row = k[1]
            elif k[0] == 'COLS:':
                col = k[1]
            elif k[0] == 'DATATYPE:':
                datatype = k[1]
    mul, D_type = (255, 'uint8') if datatype == 'U8' else ((2**16-1), 'U16')
    
    t =  (255, 'uint8') if datatype == 'U8' else ((2**16-1), 'U16')
# =============================================================================
#     print("inside the reading block\n")
#     print(type(t))
#     print(t)
#     print(mul, D_type)
# =============================================================================
    row = int(row)
    col = int(col)
    bands = int(bands)
    return row, col, bands, datatype

import matplotlib.pyplot as plt

# Reading Image file
def ReadBilFile(bil,bands,pixels):
    extract_band = 1
    image = np.zeros([pixels, bands], dtype=np.uint16)
    gdal.GetDriverByName('EHdr').Register()
    bil =str(bil)
    img = gdal.Open(bil)
# =============================================================================
#     print("\n\n\n\n printing the data returned by Open")
#     print(type(img))
#     print(img)
# =============================================================================
    
    x = 1
    while bands >= extract_band:
        bandx = img.GetRasterBand(extract_band)
        print("\n\n\nBandx data\n:--------------")
        #print(type(bandx))
        #print(bandx)
        
        datax = bandx.ReadAsArray()
        if x ==3:
            #plt.imshow(datax)
            r = datax
        if x ==4:
            #plt.imshow(datax)
            g = datax
        if x ==9:
            #plt.imshow(datax)
            b = datax
        x = x+1
        if x ==10:
           plt.figure(figsize=(150,150)) 
           r_max, r_min = r.max(),r.min()
           g_max, g_min = g.max(),g.min()
           b_max, b_min = g.max(),g.min()
           
           r_scale = ( 255*((r-r_min)/(r_max - r_min) )).astype(np.uint8)
           g_scale = ( 255*((g-g_min)/(g_max - g_min) )).astype(np.uint8)
           b_scale = ( 255*((b-b_min)/(b_max - b_min) )).astype(np.uint8)
           r_scale = r_scale.astype('uint8')
           g_scale = g_scale.astype('uint8')
           b_scale = b_scale.astype('uint8')
           print('red component: ',r_scale)
           print('green component: \n',g_scale,'\nblue component : ',b_scale )
           print("printing the image") 
           
           rgb = np.dstack((r_scale,g_scale,b_scale))
           
           
           print("Red scale :\n",r_scale)
           print("Greed scale : \n",g_scale)
           print("Blue scale :\n",b_scale)
           #plt.colorbar()
           plt.axis('off')
           #print(rgb.shape)
           #plt.axis('tight')
           plt.imshow(rgb,cmap='hot',interpolation='nearest')
           #plt.savefig('stacked_image_june19_1.png')
           plt.show()
           #plt.subplots(3,1,1)
           plt.imshow(r_scale)
           plt.subplots(3,1,2)
           plt.imshow(g_scale)
           plt.subplots(3,1,3)
           plt.imshow(b_scale)
           plt.show()

            

        #print("\nDatax data --------\n")
        #print(type(datax))
        #print(datax.shape)
        #print(datax)
        
        temp = datax
        store = temp.reshape(pixels)
        for i in range(pixels):
            image[i][extract_band - 1] = store[i]
        extract_band = extract_band + 1
    return image


from pathlib import Path

data_folder = Path("/home/sarfaraz/Desktop/isro@internship/GAN Cloud Images-20191215T170608Z-001")

# =============================================================================
file_to_open = data_folder / "stacked_june_19.hdr"
print(file_to_open)
a = hdr_read(file_to_open)  
print(type(a))
print(a)
print("rows: ",a[0], "\ncolumn : ",a[1], "\nbands : ",a[2], "\ndatatype : ",a[3])
 
 
# 
file_bil = data_folder / 'stacked_june_19'
pixels = 499*499
op1 = ReadBilFile(file_bil,a[2],  a[0]*a[1])
print(type(op1))
print(op1)
# 
bands = 10
# =============================================================================
image = np.zeros([pixels, bands], dtype=np.uint16)
# =============================================================================
# print("------------------------------------\nStacked image june 24 analysis\n")
# header_file = data_folder / 'stacked_june_24.hdr'
# b = hdr_read(header_file)
# print(type(b))
# print(b)
# print("rows : ",b[0], "\nColumn : ",b[1], "\nbands : ",b[2], "\ndatatype: ",b[3])
# 
# 
# 
# file_bil = data_folder / 'stacked_june_24'
# 
# op2 = ReadBilFile(file_bil, b[2], b[0]*b[1])
# print(type(op2))
# print(op2)
# 
# =============================================================================

























