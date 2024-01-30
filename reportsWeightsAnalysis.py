import random
from random import seed
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

# inicializações
campos = ["Reputação", "Periodicidade", "Cobertura", "Escopo", "Abrangência", "Metodologia", "Peso Final", "Score"]
camposWeights = ["p1", "p2", "p3", "p4", "p5", "p6", "acertividade"]
#pesosCampos = [1,0.6,0.2,0.2,0.1,1]
#pesosCampos = [2.2,0.8,0.6,0.6,0.8,2.2]
compArray = []

#np.arange(0, 1, 0.5)

# Gera pesos aleatórios entre 1 e 10 (possivelmente vamos reduzir a escala futuramente)
def generatorRandomWeights():
	aux = []
	for a in np.arange(0, 1, 0.1):
		for b in np.arange(0, 1, 0.1):
			for c in np.arange(0, 1, 0.1):
				for d in np.arange(0, 1, 0.1):
					for e in np.arange(0, 1, 0.1):
						for f in np.arange(0, 1, 0.1):
							aux.append([a,b,c,d,e,f])
	return aux


# Função principal
# abre os arquivos de entrada, realiza testes com os pesos e salva num arquivo
with open('scoresReports.csv', 'w', newline='') as s, open('pesosReports.csv', 'w', newline='') as p, open('comparacaoAvaliacoes.csv', 'w', newline='') as c:

	scores = csv.writer(s)
	scores.writerow(campos)
	
	pesos = csv.writer(p)
	pesos.writerow(camposWeights)
	comp = csv.writer(c)

	weights = generatorRandomWeights()
	#print(weights)
	for pesosCampos in weights:

		somaWeights = 0
		for item in pesosCampos :
			somaWeights += item
		
			
		count = 0
		equal = 0
		diff = 0
		
		with open('entradaEmpresas.csv') as entrada:

			csv_reader = csv.reader(entrada, delimiter=',')

			for linha in csv_reader:
				count += 1

				reputacao = int(linha[0])
				periodicidade = int(linha[1])
				cobertura = int(linha[2])
				escopo = int(linha[3])
				abrangencia = int(linha[4])
				metodologia = int(linha[5])
				
				company = [reputacao, periodicidade, cobertura, escopo, abrangencia, metodologia]
				
				pesoFinal = ((reputacao*pesosCampos[0])  + (periodicidade*pesosCampos[1]) + (cobertura*pesosCampos[2]) + (escopo*pesosCampos[3]) + (abrangencia*pesosCampos[4]) + (metodologia*pesosCampos[5]))/(somaWeights)*3.0
				print(pesoFinal)
				
				if pesoFinal >= 5 :
					rating = "Ótimo" # Muito Relevante
				elif pesoFinal >= 3 :
					rating = "Bom" # Relevante
				else :
					rating = "Ruim" # Pouco Relevante
					
				company.append(round(pesoFinal, 2))
				company.append(rating)

				#comparando o gerad
				compArray = [linha[6], linha[7], company[6], company[7], linha[8]]
				if compArray[3] == compArray[4]:
					equal += 1

				comp.writerow(compArray)
				scores.writerow(company)
				
			nota = [equal/count*100]
			conf1 = conf2 = False
			if pesosCampos[2] > pesosCampos[1] and pesosCampos[2] > pesosCampos[3] and pesosCampos[2] > pesosCampos[4]:
				conf1 = True
			if pesosCampos[2] < pesosCampos[0] and pesosCampos[2] < pesosCampos[5]:
				conf2 = True
			if nota[0] > 10.0 and conf1 and conf2:				
				pesos.writerow(pesosCampos+nota)


