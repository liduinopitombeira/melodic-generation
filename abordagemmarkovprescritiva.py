# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 00:05:10 2023

@author: Liduino Pitombeira
"""

from music21 import *
from random import *
import numpy as np
import pandas as pd
from copy import *


#Matriz de transição
def MatrixTransition(M):
                   
    #Normaliza a matriz
    for j in range(len(M)):
        total = sum(M[j])
        for k in range(len(M)):
            M[j][k] = round((M[j][k])/total,20)
    
    return(M)


# Lê o arquivo Excel.
excel_file = 'tabelapres.xlsx'

# Use a função read_excel para ler os dados do arquivo Excel.
df = pd.read_excel(excel_file, sheet_name='matrizcontagem', index_col=0)

# Converter o DataFrame em um array NumPy
R = df.values

# Converter o array NumPy em uma lista
R = R.tolist()

# Obter os valores da primeira linha (nomes de coluna) como uma lista
linha = df.columns.tolist()

Original = deepcopy(R)

N = MatrixTransition(R)


# Sorteando através da matriz de transição

# Valor inicial
Bset = linha
Bset.sort()
nota = np.random.choice(Bset, 1, True)
print('nota sorteada inicial = ',nota)

qte = 0
nova =[]

while qte < 100:
    nova.append(nota)
    nota = np.random.choice(Bset, 1, True, N[Bset.index(nota)])
    qte = qte + 1

# Convertendo as arrays para inteiros
nova = [int(nova[i]) for i in range(len(nova))]

print('Nova melodia = ', nova)

durations = [0.5, 1, 2]

melodic_line = stream.Stream()

for i in range(len(nova)):
    nota = note.Note(nova[i])
    if i<len(nova):
        nota.quarterLength = choice(durations)
    else:
        nota.quarterLength = 2
    melodic_line.append(nota)
    

melodic_line.write('mxl', 'novamelodiaprescritiva2024.mxl')
