from music21 import *
import random  

# Lista de acordes com notas
acordes = [[60,64,67],[68,71,75],[63,67,70],[59,63,68],[58,61,65],
           [65,69,72],[58,62,65]]


# Cria duas partes (melodia e acordes)
composicao2 = stream.Part()
chords = stream.Part()

#Durações disponíveis
durations_disponiveis = [0.5, 1]

# O número de compassos desejado depende da quantidade de acordes
num_compassos = len(acordes)

#Inicializa as listas
#notas_escolhidas para verificar no final que notas foram escolhidas
notas_escolhidas = []
#durações escolhidas para cada compasso
measure_durations = []

# Gere os compassos com durações de notas aleatórias
for i in range(num_compassos):
    #Cria o objeto compasso para guardar as notas
    compasso = stream.Measure()
    
    # Gera um número aleatório de notas para cada compasso
    # O último compasso terá apenas uma nota
    if i == len(acordes)-1: num_notas = 1
    else: num_notas = random.randint(3, 6)
    
    # Gera o número de figuras rítmicas para cada compasso
    # O último compasso terá uma figura rítmica longa
    if i == len(acordes)-1: durations = [3]
    else: durations = random.choices(durations_disponiveis, k=num_notas)
    
    #Calcula a duração total do compasso e preenche a lista
    compasso_duration = sum(durations)
    measure_durations.append(compasso_duration)
    
    #Designa a métrica com base no tamanho do compasso
    numerador = str(int(compasso_duration*2))
    denominador = '/8'
    
    #Guarda o valor no objeto compasso
    compasso.append(meter.TimeSignature(numerador + denominador))
   
    print(durations)
    
    #Acopla notas às figuras rítmicas e guarda no objeto compasso
    #e na lista notas_escolhidas
    for j in range(num_notas):
        nota_escolhida = random.choice(acordes[i])
        nota_aleatoria = note.Note(nota_escolhida)
        if num_notas == 1:nota_aleatoria.quarterLength = compasso_duration
        else: nota_aleatoria.quarterLength = durations[j]
        compasso.append(nota_aleatoria)
        notas_escolhidas.append(nota_escolhida)
    
    #Terminado o loop guarda o compasso na parte
    composicao2.append(compasso)
    
#Lista na tela as métricas escolhidas para cada compasso
timesignatures = []

for k in composicao2:
    timesignatures.append(k[0])
    print(k[0])

# Cria parte de acordes
linha_acordes = stream.Part()

# Insere os acordes com a mesma métrica melódica 
for i in range(len(acordes)):
    m = stream.Measure()
    m.timeSignature = timesignatures[i]
    c = chord.Chord(acordes[i])
    c.duration = duration.Duration(measure_durations[i])
    m.append(c)
    
    linha_acordes.append(m)
    
    
# Cria uma partitura para exibir a melodia e os acordes simultaneamente
partitura = stream.Score()
partitura.insert(0, composicao2)
partitura.insert(0, linha_acordes)

# Grava a partitura
partitura.write('mxl', 'abvert2b.mxl')
