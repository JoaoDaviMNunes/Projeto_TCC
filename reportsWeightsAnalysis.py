from random import seed
from random import randint
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

# inicializações
companyWeights = []
campos = ["Reputação", "Periodicidade", "Cobertura", "Escopo", "Abrangência", "Metodologia", "Peso Final", "Score"]
pesosCampos = [0.8,0.3,0.3,0.3,0.3,0.8]
start = 0
end = 2

with open('scoresReports.csv', 'w', newline='') as s, open('pesosReports.csv', 'w', newline='') as p, open('entradaEmpresas.csv') as entrada:
	
	csv_reader = csv.reader(entrada, delimiter=',')
	scores = csv.writer(s)
	scores.writerow(campos)
	pesos = csv.writer(p)

	weights = pesosCampos
	somaWeights = 0

	for item in pesosCampos :
		somaWeights += item

	
	pesos.writerow(pesosCampos)
		
	count = 0
	for row in csv_reader:
		if count != 0 :
			reputacao = int(row[0])
			periodicidade = int(row[1])
			cobertura = int(row[2])
			escopo = int(row[3])
			abrangencia = int(row[4])
			metodologia = int(row[5])
			
			company = [reputacao, periodicidade, cobertura, escopo, abrangencia, metodologia]
			
			pesoFinal = ((reputacao*weights[0])  + (periodicidade*weights[1]) + (cobertura*weights[2]) + (escopo*weights[3]) + (abrangencia*weights[4]) + (metodologia*weights[5]))/(somaWeights)*3.0
			
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
			
			scores.writerow(company)
		
		count += 1
		
