#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:31:22 2020

@author: sarfaraz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:03:15 2019

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




def ReadBilFile(bil):#,pixels):
    extract_band = 1
    #image = np.zeros([pixels, bands], dtype=np.uint16)
    gdal.GetDriverByName('EHdr').Register()
    bil =str(bil)
    img = gdal.Open(bil)
    
    bandx = img.GetRasterBand(extract_band)
    datax = bandx.ReadAsArray();
    
    print("type of bandx: ",type(datax))
  
    print("\nshape of data :",datax.shape)
   
    data = np.array(datax)
    return data
  
from pathlib import Path
data_folder = Path("/home/sarfaraz/Desktop/isro@internship/task3/False_band_2")

file_to_open = data_folder / "band_2.hdr"
a = hdr_read(file_to_open)  

print(type(a))
print(a)
print("rows: ",a[0], "\ncolumn : ",a[1], "\nbands : ",a[2], "\ndatatype : ",a[3])

file_bil = data_folder / 'band_2'
pixels = 499
raw_false_image = ReadBilFile(file_bil)
r_min = raw_false_image.min()
r_max = raw_false_image.max()
false_image =  ( 255*((raw_false_image-r_min)/(r_max - r_min) )).astype(np.uint8)
print(type(false_image))
print(false_image)
# 
print(type(false_image), "\nshape:========== \n")


data_folder = Path("/home/sarfaraz/Desktop/isro@internship/task3/True_band_2")
file_to_open= data_folder/"sub_june_19_band_2"

raw_true_image = ReadBilFile(file_to_open)
t_min , t_max = raw_true_image.min(), raw_true_image.max()
true_image = ( 255*((raw_true_image-t_min)/(t_max - t_min) )).astype(np.uint8)


# save numpy array as csv file
from numpy import asarray
from numpy import savetxt
savetxt('true_image.csv', true_image, delimiter=',')
savetxt('false_image.csv', false_image, delimiter=',')



# load numpy array from csv file
from numpy import loadtxt
# load array
# =============================================================================
# l_true_image= loadtxt('raw_true_image.csv', delimiter=',')
# l_false_image = loadtxt('raw_false_image.csv',delimiter=',')
# 
# =============================================================================





# =============================================================================
# 
# plt.subplot(231)
# cmap = 'gray'
# plt.figure(figsize=(15,10))
# plt.imshow(l_true_image, cmap=cmap,interpolation='nearest')
# plt.axis('off')
# plt.title('true image')
# plt.show()
# 
# plt.subplot(232)
# cmap = 'gray'
# plt.figure(figsize=(15,10))
# plt.imshow(l_false_image, cmap=cmap,interpolation='nearest')
# plt.axis('off')
# plt.title('true image')
# plt.show()
# 
# =============================================================================
