# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 22:33:44 2023

@author: Liduino Pitombeira
"""

from music21 import *
from random import *
from copy import *


def INV(serie):
    
    inversa = [(12-x)%12 for x in serie]
    return inversa
    

def TRANS (serie):
    
    intervalos = range(1,12)
    fator = choice(intervalos)
    transposta = [(fator + x) for x in serie]
    return transposta
    
def RET(serie):
    
    return serie[::-1]

#================================================

cromas = list(range(0,12,1))

serie = deepcopy(cromas)
shuffle(serie)

melodia = INV(serie)+serie+TRANS(serie)+RET(serie)+RET(INV(serie))

linha = stream.Stream()

for x in range(len(melodia)):
    nota = note.Note(melodia[x]+60)
    nota.quarterLength = choice([0.5,1,1.5])
    linha.append(nota)
    
linha.show()    

