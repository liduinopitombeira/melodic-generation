# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 00:13:27 2023

@author: Liduino Pitombeira
"""

from random import *
from music21 import *

quantidade = 20

alturas = [x for x in range(60, 71, 1)]

linha = [choice(alturas) for x in range(quantidade)]

melodia = stream.Stream()

for x in range(len(linha)):
    nota = note.Note(linha[x])
    quarterLength = 1
    melodia.append(nota)
    
# melodia.write(".mxl", "melodia.mxl")

melodia.show()
