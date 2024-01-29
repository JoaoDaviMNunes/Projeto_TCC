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
pesosCampos = [1,0.5,0.5,0.5,0.5,0.9]
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
		
	count = 0
	equal = 0
	diff = 0
	for row in csv_reader:
		if count != 0 :
			reputacao = int(row[0])
			periodicidade = int(row[1])
			cobertura = int(row[2])
			escopo = int(row[3])
			abrangencia = int(row[4])
			metodologia = int(row[5])
			
			company = [reputacao, periodicidade, cobertura, escopo, abrangencia, metodologia]
			
			pesoFinal = ((reputacao*pesosCampos[0])  + (periodicidade*pesosCampos[1]) + (cobertura*pesosCampos[2]) + (escopo*pesosCampos[3]) + (abrangencia*pesosCampos[4]) + (metodologia*pesosCampos[5]))/(somaWeights)*3.0
			
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
			
			if float(compArray[0]) < compArray[2]:
				compArray.append("+")
				diff += 1
			elif float(compArray[0]) > compArray[2]:
				compArray.append("-")
			else :
				compArray.append("=")

			comp.writerow(compArray)
			scores.writerow(company)
		
		count += 1

	print(count)
	print(equal)
	print(equal/count*100)		
