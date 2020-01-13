#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:57:42 2019

@author: sarfaraz
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

image_name = 'minion.png';

im_data = img.imread(image_name)
print('original image data\n',im_data)
print(im_data.shape)
print(type(im_data))
print(im_data.dtype)


# =============================================================================
# plt.subplot(231)
# cmap='gray'
# plt.figure(figsize=(15,10))
# plt.imshow(im_data, cmap = cmap, interpolation='nearest')
# plt.axis('off')
# plt.title('original image')
# =============================================================================
# =============================================================================
plt.subplot(232)
plt.figure(figsize=(15,10))
red_data = im_data[:,:,0]
green_data = im_data[:,:,1]
blue_data = im_data[:,:,2]
# =============================================================================
# plt.axis('off')
# plt.imshow(im_data)
# =============================================================================
# #very important to swap axes
bgr_data = np.array([(1.5*blue_data), (1.5*green_data), (1.*red_data)])
bgr_data = np.swapaxes(bgr_data, 0,1)
bgr_data = np.swapaxes(bgr_data, 1, 2)
print(bgr_data.shape)
plt.axis('off')
plt.title('bgr image')
plt.imshow(bgr_data)
#plt.show()
# =============================================================================
# plt.subplot(233)
# plt.figure(figsize=(15,10))
# =============================================================================
# =============================================================================
# grb_data = np.array([green_data, red_data, blue_data])
# grb_data = np.swapaxes(grb_data,0,1)
# grb_data= np.swapaxes(grb_data,1,2)
# print(grb_data.shape)
# plt.axis('off')
# plt.title('grb_data')
# plt.imshow(grb_data)
# =============================================================================




# 
# 
# 
# A = np.array([[1,1,2],[1,2,1]])
# plt.pcolor(A,cmap='Blues')
# plt.colorbar()
# =============================================================================
plt.show()