# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:25:58 2020

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
from random import *


def mandel(R,I,max_iter):
    
    c = complex(R,I)
    z = 0.0j
    count=0
    modulo=0
    
        
    while modulo<=4 and count<max_iter:
    
        z = z*z + c
        modulo = (z.real*z.real + z.imag*z.imag)
        count = count+1
        
    return(count)    


#Fix the number of rows and columns
rows=200
columns = 200

#Creates an array of zeros
arr = np.zeros([rows,columns])

print(arr)


#Sweeps all the points in a plane (rows x columns). Each
#point is complex number

for row_index, I in enumerate (np.linspace(-1,1,num=rows)):
    for column_index, R in enumerate(np.linspace(-2,1,num=columns)):
                
        arr[row_index,column_index] = mandel(R,I,100)
        

print(arr)


plt.imshow(arr, cmap='Greys',interpolation = 'bilinear', extent = [-2,1,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.savefig('mandelbw.pdf',dpi=1200)
