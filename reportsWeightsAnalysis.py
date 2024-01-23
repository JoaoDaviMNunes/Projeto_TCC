from random import seed
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

# inicializações
companyWeights = []
campos = ["Reputação", "Periodicidade", "Cobertura", "Escopo", "Abrangência", "Metodologia", "Peso Final", "Score"]

with open('testePesosReports.csv', 'w', newline='') as f :
	
	writer = csv.writer(f)
	writer.writerow(campos)
	
	for _ in range(10000):
		reputacao = randint(0,2)
		periodicidade = randint(0,2)
		cobertura = randint(0,2)
		escopo = randint(0,2)
		abrangencia = randint(0,2)
		metodologia = randint(0,2)
		company = [reputacao, periodicidade, cobertura, escopo, abrangencia, metodologia]
		pesoFinal = (reputacao + periodicidade + cobertura + escopo + abrangencia + metodologia)/2
		
		'''
		print(companyWeights)
		print(pesoFinal)
		'''
			

		
		if pesoFinal >= 5 :
			score = "Ótimo"
		elif pesoFinal >= 3 :
			score = "Bom"
		elif pesoFinal < 1 :
			pesoFinal = 1.0
			score = "Ruim"
		else :
			score = "Ruim"
			
		company.append(pesoFinal)
		company.append(score)
		
		writer.writerow(company)
		
