from music21 import *
from random import *

def mapear_para_alturas(texto):
    tabela = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
        'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 0,
        'N': 1, 'O': 2, 'P': 3, 'Q': 4, 'R': 5, 'S': 6,
        'T': 7, 'U': 8, 'V': 9, 'W': 10, 'X': 11, 'Y': 12, 'Z': 13
    }

    listas_de_classes_de_alturas = []
    alturas = []

    for caractere in texto:
        if caractere.upper() in tabela:
            alturas.append(tabela[caractere.upper()])
        elif caractere.isspace():
            if alturas:
                listas_de_classes_de_alturas.append(alturas)
                alturas = []
        else:
            alturas.append(None)  # Caso o caractere não esteja na tabela

    if alturas:
        listas_de_classes_de_alturas.append(alturas)

    return listas_de_classes_de_alturas

# Exemplo de uso:
entrada = input('Entre com uma frase: ')
listas_de_classes_de_alturas = mapear_para_alturas(entrada)

print(f"Texto de entrada: {entrada}")
print(f"Listas de classes de alturas: {listas_de_classes_de_alturas}")

flatlist = sum(listas_de_classes_de_alturas, [])

melodia = stream.Stream()

for i in flatlist:
    nota = note.Note(i)
    nota.quarterLength = choice([0.5,1])
    melodia.append(nota)
    
# melodia.write('musicxml', 'colegio.musicxml')    

melodia.show()