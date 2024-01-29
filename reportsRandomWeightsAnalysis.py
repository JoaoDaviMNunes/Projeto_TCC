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
pesosCampos = [0.8,0.4,0.5,0.5,0.1,0.8]
compArray = []

with open('scoresReports.csv', 'w', newline='') as s, open('pesosReports.csv', 'w', newline='') as p, open('entradaEmpresas.csv') as entrada, open('comparacaoAvaliacoes.csv', 'w', newline='') as c:
	
	csv_reader = csv.reader(entrada, delimiter=',')

	scores = csv.writer(s)
	scores.writerow(campos)
	
	pesos = csv.writer(p)
	comp = csv.writer(c)

	somaWeights = 0
	for item in pesosCampos :
		somaWeights += item
	
	pesos.writerow(pesosCampos)

	randomPesos = []
	for _ in range(6) :
		pes1 = random.random()
		pes2 = random.random()
		pes3 = random.random()
		pes4 = random.random()
		pes5 = random.random()
		pes6 = random.random()
		randomPesos.append([pes1, pes2, pes3, pes4, pes5, pes6])
	
	for pes in randomPesos:
		print(pes)
		count = 0
		equal = 0
		for row in csv_reader:
			if count != 0 :
				reputacao = int(row[0])
				periodicidade = int(row[1])
				cobertura = int(row[2])
				escopo = int(row[3])
				abrangencia = int(row[4])
				metodologia = int(row[5])
				
				company = [reputacao, periodicidade, cobertura, escopo, abrangencia, metodologia]
				
				pesoFinal = ((reputacao*pes[0])  + (periodicidade*pes[1]) + (cobertura*pes[2]) + (escopo*pes[3]) + (abrangencia*pes[4]) + (metodologia*pes[5]))/(somaWeights)*3.0
				
				
				if pesoFinal >= 5 :
					rating = "Ótimo"
				elif pesoFinal >= 3 :
					rating = "Bom"
				elif pesoFinal < 1 :
					pesoFinal = 1.0
					rating = "Ruim"
				else :
					rating = "Ruim"
					
				company.append(round(pesoFinal, 2))
				company.append(rating)

				compArray = [row[6], row[7], company[6], company[7]]
				if compArray[1] == compArray[3]:
					equal += 1
				comp.writerow(compArray)
				
				scores.writerow(company)
			
			count += 1

			print(count)
			print(equal)
			print(equal/count*100)		
