# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:34:41 2023

@author: Liduino Pitombeira
"""

from random import *
from music21 import *

#Nota(n) e sentido(s), ascendente ou descendente
def S(n,s):
    
    nota = n + s*(choice(range(3,12,1)))
    return nota
    
#Nota(n) e sentido(s), ascendente ou descendente
def C(n,s):
    
    nota = n + s*(choice(range(1,3,1)))
    
    return nota    


#Nota(n) e sentido(s), ascendente ou descendente
def R(n):
    
    return n 

#Gera fragmento com base no ciclo e no tamanho fornecido pelo usuário
def GERA(n, ciclo):
    
    nota_inicial = choice(list(range(52,85,1)))
    A = [nota_inicial]
    sentido = [1,-1]
    
    k = 0 
    
    while k<n:
    
        for i in ciclo:
            
            if i == 'S':
                sen = choice(sentido)
                nota_inicial = S(A[-1], sen)
                if nota_inicial > 85:
                    nota_inicial = 85-12
                A.append(nota_inicial)
                
            elif i == 'C':
                
                sen = choice(sentido)
                nota_inicial = C(nota_inicial, sen)
                if nota_inicial > 85:
                    nota_inicial = 85-12
                A.append(nota_inicial)
                
            else:
                
                nota_inicial = R(nota_inicial)
                A.append(nota_inicial)
                
        k = k + 1
        
    return A


print ("===========")
print ("SISTEMA SCR")
print ("===========")
print ("Esse sistema produz notas com base em três tipos de movimentos: S - salto, C - grau conjunto e R - repetição")

n = int(input('Entre com o valor de n (tamanho do ciclo): '))
ciclo = input('Entre com o ciclo operacional (Exemplo SCCRCC): ')

A = GERA(n,ciclo)
melodia_A = stream.Stream() 
 

for i in range(len(A)):
    
    nota = note.Note(A[i])
    if i<(len(A)-1): 
        nota.quarterLength = choice([0.5,1,1.5])
    else: nota.quarterLength = 2
    melodia_A.append(nota)
    
melodia_A.show()

