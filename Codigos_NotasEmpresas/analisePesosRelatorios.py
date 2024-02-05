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
camposWeights = ["p1", "p2", "p3", "p4", "p5", "p6", "precisão"]
compArray = []

# Gera pesos aleatórios entre 1 e 10
def generatorRandomWeights():
	aux = []
	for rep in np.arange(1, 11, 1):
		for per in np.arange(1, 11, 1):
			for cob in np.arange(1, 11, 1):
				for esc in np.arange(1, 11, 1):
					for abr in np.arange(1, 11, 1):
						for met in np.arange(1, 11, 1):
							aux.append([rep,per,cob,esc,abr,met])
	return aux

# ===========================================================================
# Função principal
# abre os arquivos de entrada, realiza testes com os pesos e salva num arquivo
# Entrada:
# entradaEmpresas.csv = [6 notas de 0 a 2,notaSoma,notaEmpirica]
# Saídas:
# scoresReports.csv = [rep,per,cob,esc,abr,met,notaCPeso,scoreCPeso] p/ cada empresa
# pesosReports.csv = [p1,p2,p3,p4,p5,p6,precisao] (pesosCampos+precisao)
# comparacaoAvaliacoes.csv = [notaOriginal,scoreOriginal,notaCPeso,scoreCPeso,scoreEmpirico]
with open('scoresReports.csv', 'w', newline='') as s, open('pesosReports.csv', 'w', newline='') as p, open('comparacaoAvaliacoes.csv', 'w', newline='') as c:

	scores = csv.writer(s)
	scores.writerow(campos)
	
	pesos = csv.writer(p)
	pesos.writerow(camposWeights)
	comp = csv.writer(c)

	weights = generatorRandomWeights()
	for pesosCampos in weights:

		somaWeights = 0
		for item in pesosCampos :
			somaWeights += item
			
		count = 0	# conta o número de empresas
		equal = 0	# conta o número de empresas com a mesma nota (antes e depois)
		
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
				# print(pesoFinal)
				
				if pesoFinal >= 5 :
					rating = "MuitoRelevante"
				elif pesoFinal >= 3 :
					rating = "Relevante"
				else :
					rating = "PoucoRelevante"
					
				company.append(round(pesoFinal, 2))
				company.append(rating)

				#comparando as notas originais das Empresas com o calculado usando os pesos
				# linha[6] = notaOriginal
				# linha[7] = scoreOriginal
				# company[6] = notaCPeso
				# company[7] = scoreCPeso
				# linha[8] = scoreEmpirico
				compArray = [linha[6], linha[7], company[6], company[7], linha[8]]
				# verifica se a nota empírica corresponde à nota com peso
				if compArray[3] == compArray[4]:
					equal += 1

				comp.writerow(compArray)
				scores.writerow(company)
				
			precisao = [equal/count*100]
			conf1 = conf2 = False
			if pesosCampos[2] > pesosCampos[1] and pesosCampos[2] > pesosCampos[3] and pesosCampos[2] > pesosCampos[4]:
				conf1 = True
			if pesosCampos[2] < pesosCampos[0] and pesosCampos[2] < pesosCampos[5]:
				conf2 = True
			if precisao[0] > 10.0 and conf1 and conf2:				
				pesos.writerow(pesosCampos+precisao)

