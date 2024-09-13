from music21 import *
from random import *
from copy import *


#Função que realiza o retrógrado da célula
def R(lista):
    listacopy= deepcopy(lista)
    novalista = listacopy[::-1]
    return novalista

#Função que inverte a célula em torno da nota inicial diatonicamente
def I(lista):
    alturas = [48,50,52,53,55,57,59,60,62,64,65,67,69,71,72,74,76,77,79,81,83,84]
    indices = [alturas.index(alturas[x]) for x in range(len(alturas))]
    listacopy= deepcopy(lista)
    listatraduzida = [alturas.index(x) for x in listacopy]
    intervalos = [listatraduzida[x+1] - listatraduzida[x] for x in range(len(listatraduzida)-1)]
    intervalosinversos = [-i for i in intervalos]
    
    novalista = [listatraduzida[0]]
    
    for i in range(len(intervalosinversos)):
       novalista.append(novalista[i] + intervalosinversos[i])
       
    novalistaretraduzida = [alturas[x] for x in novalista]   
       
    return novalistaretraduzida    

#Função que transpõe diatonicamente uma lista de alturas por um fator k
def T(lista,k):
    if k>0: k = k - 1
    else: k = k + 1
    
    alturas = [48,50,52,53,55,57,59,60,62,64,65,67,69,71,72,74,76,77,79,81,83,84]
    indices = [alturas.index(alturas[x]) for x in range(len(alturas))]
    listacopy= deepcopy(lista)
    listatraduzida = [alturas.index(x) for x in listacopy]
    novalista = [x + k for x in listatraduzida]
    
    novalistaretraduzida = [alturas[x] for x in novalista]   
       
    return novalistaretraduzida    
    

# Células básicas (tessitura máxima: G3 - G5, sendo C4 o C central)
# A = [69,74,72]
# B = [71,64,65,69]

A = input('Entre com uma lista de números MIDI diatônicos (de 59 a 76) separados por espaço: ').split()
A = [int(x) for x in A]

B = input('Entre com uma lista de números MIDI diatônicos (de 59 a 76) separados por espaço: ').split()
B = [int(x) for x in B]

Ciclo = input('Entre com um ciclo: ')

Lista = (eval(Ciclo))
print(Lista)

Listacromatica = [x+choice([0,0,0,1,1,-1]) for x in Lista]

partitura = stream.Stream()

for x in Listacromatica:
    nota = note.Note(x)
    partitura.append(nota)
    
partitura.show()    




