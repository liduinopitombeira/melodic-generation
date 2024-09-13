# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:25:58 2020

@author: Liduino Pitombeira
"""

from music21 import *
import matplotlib.pyplot as plt
import numpy as np
from random import *


# =============================================================================
# ITERATION FUNCTION
# =============================================================================

def mandel(R,I,max_iter):
    
    c = complex(R,I)
    z = 0.0j
    count=0
  
    while abs(z)<=2 and count<max_iter:
    
        z = z*z + c
        count = count+1
 
    return[count, c, abs(z)]    

# =============================================================================
# THE MAIN PROGRAM
# =============================================================================

#Fix the number of rows and columns
rows=20
columns = 20
resultado=[]

#Creates an array of zeros
matriz = np.zeros([rows,columns])


#Sweeps all the points in a plane (real=1,1, Imag = -2,1). Each
#point is complex number

for row_index, I in enumerate (np.linspace(-1,1,num=rows)):
    for column_index, R in enumerate(np.linspace(-2,1,num=columns)):
        
        mandelset = mandel(R,I,100)      
        matriz[row_index,column_index] = mandelset[0]
        resultado.append(mandelset)

# =============================================================================
# PRODUCES THE IMAGE IN 600 DPI
# =============================================================================

plt.imshow(matriz, cmap='Greys',interpolation = 'bilinear', extent = [-2,1,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.savefig('mandelbw3.pdf',dpi=600)

# =============================================================================
# LIST THE MEMBERS OF THE MANDELBROT SET AND EXTRACT REAL AND IMAG PARTS
# =============================================================================

altura=[]
ritmo=[]

for j in range(len(resultado)):
    if resultado[j][2]<=2:
        mandel=resultado[j][1]
        altura.append(mandel.real)
        ritmo.append(mandel.imag)

# =============================================================================
# NORMALIZE THE VALUES OF PITCH AND DURATION
# =============================================================================

alturas_normalizadas = [int(round(x*10,0))%12 for x in altura]
ritmos_normalizados = [abs(round(x*10))*0.25 for x in ritmo]

print(alturas_normalizadas)  
print('===============')
print(ritmos_normalizados)

# =============================================================================
# SENDS PITCH AND DURATION TO MUSIC21
# =============================================================================

melodia = stream.Stream()

for i in range(len(alturas_normalizadas)):
    nota = note.Note(alturas_normalizadas[i])
    nota.quarterLength = ritmos_normalizados[i]
    melodia.append(nota)


melodia.write('midi', 'feedmandel7.mid')
