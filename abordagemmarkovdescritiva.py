# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 00:05:10 2023

@author: Liduino Pitombeira
"""

from music21 import *
from random import *
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Graph


#Matriz de contagem
def MatrixTransitionraw(A):
    
    #List with unique values of A and in ascending order 
    Aset = list(set(A))
    Aset.sort()

    #List of list filled with zeros (this will be filled by the iteractions)
    M = [[0]*len(Aset) for i in range(len(Aset))]

    #Gera a matriz de transição de probabilidades
    for i in range(len(A)-1):
        pos_linha = Aset.index(A[i])
        pos_coluna = Aset.index(A[i+1])
        M[pos_linha][pos_coluna]+=1
        
        
    return(M)

#Matriz de transição
def MatrixTransition(A):
    
    #List with unique values of A and in ascending order 
    Aset = list(set(A))
    Aset.sort()

    #List of list filled with zeros (this will be filled by the iteractions)
    M = [[0]*len(Aset) for i in range(len(Aset))]

    #Gera a matriz de transição de probabilidades
    for i in range(len(A)-1):
        pos_linha = Aset.index(A[i])
        pos_coluna = Aset.index(A[i+1])
        M[pos_linha][pos_coluna]+=1
        
    #Normaliza a matriz
    for j in range(len(M)):
        total = sum(M[j])
        for k in range(len(M)):
            M[j][k] = round((M[j][k])/total,2)
    
    return(M)


#Extract the pitch parameter from a MIDI file
piece = converter.parse("jm_.mxl")
dados = [x.pitch.midi for x in piece.stripTies().flat.getElementsByClass('Note')]
  
print('Melodia original ',dados)

#Matriz de contagem
R = MatrixTransitionraw(dados)
print('Matriz de contagem = ', R)

#Matriz de transição
N = MatrixTransition(dados)
print('Matriz de transição = ', N)

linha = list(set(dados))
linha.sort()
print('linha', linha)

#Tabela excel dos movimentos melódicos

df = pd.DataFrame(R, index=linha, columns=linha)
writer = pd.ExcelWriter('tabelajmraw.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Planilha1')
writer.save()

#Matriz de transição no formato excel

df = pd.DataFrame(N, index=linha, columns=linha)
writer = pd.ExcelWriter('tabelajm.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Planilha1')
writer.save()


#Desenhando um grafo dos movimentos entre notas

# Converta a lista linha em um array numpy
R = np.array(R)

# Crie o objeto grafo
g = Graph(format='svg')

# Adicione os vértices com os rótulos da lista linha
for i in range(len(linha)):
    g.node(str(i), str(linha[i]))

# Adicione as arestas com pesos da matriz de transição N (exceto se o peso for zero)
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        peso = R[i][j]
        if peso != 0:
            g.edge(str(i), str(j), label=str(peso), dir='forward')

# Salve o grafo em um arquivo SVG
g.render('grafojmabsoluto')


#Desenhando um grafo da matriz de transição

# Converta a lista linha em um array numpy
N = np.array(N)

# Crie o objeto grafo
g = Graph(format='svg')

# Adicione os vértices com os rótulos da lista linha
for i in range(len(linha)):
    g.node(str(i), str(linha[i]))

# Adicione as arestas com pesos da matriz de transição N (exceto se o peso for zero)
for i in range(N.shape[0]):
    for j in range(N.shape[1]):
        peso = N[i][j]
        if peso != 0:
            g.edge(str(i), str(j), label=str(peso), dir='forward')

# Salve o grafo em um arquivo SVG
g.render('grafojm')

# Sorteando através da matriz de transição

# Valor inicial
Bset = list(set(dados))
Bset.sort()
nota = np.random.choice(Bset, 1, True)
print('nota sorteada inicial = ',nota)

qte = 0
nova =[]

while qte < 30:
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
    

# melodic_line.write('mxl', 'novamelodiajm.mxl')

melodic_line.show()
