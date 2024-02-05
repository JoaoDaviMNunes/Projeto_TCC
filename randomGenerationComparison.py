import random
from random import seed
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics
import math
from sklearn.metrics import confusion_matrix
import seaborn as sns

# ================================================================================================
# VARIÁVEIS
# ================================================================================================

QNTD_EMP = 10000
MAGIC_NUMBER = 5
pesoEscolhido = [10,5,8,6,5,10] # [pes_rep,pes_per,pes_cob,pes_esc,pes_abr,pes_met], um dos que fazer 95% de precisão
notasPossiveis = ["PoucoRelevante","Relevante","MuitoRelevante"]

# ================================================================================================
# FUNÇÕES AUXILIARES
# ================================================================================================

# Avalia uma empresa e retorna a nota
def notaEmpresas(total):
	if total >= 5 :
		nota = "MuitoRelevante"
	elif total >= 3 :
		nota = "Relevante"
	else :
		nota = "PoucoRelevante" 
	#print(nota)
	return nota

# Calcula qual seria a nota da empresa dada os pesos escolhidos e retorna
def notaEmpresasPeso(lista):
	argCima = lista[0]*pesoEscolhido[0] + lista[1]*pesoEscolhido[1] + lista[2]*pesoEscolhido[2] + lista[3]*pesoEscolhido[3] + lista[4]*pesoEscolhido[4] + lista[5]*pesoEscolhido[5]
	argBaixo = pesoEscolhido[0] + pesoEscolhido[1] + pesoEscolhido[2] + pesoEscolhido[3] + pesoEscolhido[4] + pesoEscolhido[5]
	arg = argCima/argBaixo*3
	novaNota = notaEmpresas(arg)
	return novaNota

# ================================================================================================
# CÓDIGO PRINCIPAL
# ================================================================================================

# Gera valores de empresa randômicos e verifica se são falsos positivos ou negativos
# e armazena numa lista para futuramente plotar
# Saídas:
# randomCompanies.csv = [rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso]
with open('randomCompanies.csv', 'w', newline='') as r:
	rc = csv.writer(r) # abre o arquivo para poder escrever
	
	dadosRodadas = []	# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda todos os dados das rodadas
	maximo = []	# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda a rodada com maior precisao
	minimo = []	# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda a rodada com menor precisao

	for rodadas in range(MAGIC_NUMBER):
		diffP = 0
		diffN = 0
		equal = 0

		pp,pr,pm = 0,0,0 # somatorio de transição do estado "PoucoRelevante"
		rp,rr,rm = 0,0,0 # somatorio de transição do estado "Relevante"
		mp,mr,mm = 0,0,0 # somatorio de transição do estado "MuitoRelevante"

		#falsosP =	[]
		#falsosN =	[]
		#iguais =	[]

		# gera 10000 empresas randômicas
		for i in range(QNTD_EMP):
			rep = random.randint(0,2)
			per = random.randint(0,2)
			cob = random.randint(0,2)
			esc = random.randint(0,2)
			abr = random.randint(0,2)
			met = random.randint(0,2)

			somatorio = (rep+per+cob+esc+abr+met)/2
			notaOriginal = notaEmpresas(somatorio)
			notaPeso = notaEmpresasPeso([rep,per,cob,esc,abr,met])

			conf = notasPossiveis.index(notaPeso) - notasPossiveis.index(notaOriginal)
			#print(notaOriginal + " || " + str(conf) + " || " + notaPeso)
			if notaOriginal == "PoucoRelevante":
				if conf == 0:
					#iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					equal += 1
					pp += 1
				elif conf == 1:
					#falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffP += 1
					pr += 1
				elif conf == 2:
					#falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffP += 1
					pm += 1
					print("pm")
			elif notaOriginal == "Relevante":
				if conf == 0:
					#iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					equal += 1
					rr += 1
				elif conf == -1:
					#falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffN += 1
					rp += 1
				elif conf == 1:
					#falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffP += 1
					rm += 1
			elif notaOriginal == "MuitoRelevante":
				if conf == 0:
					#iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					equal += 1
					mm += 1
				elif conf == -1:
					#falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffN += 1
					mr += 1
				elif conf == -2:
					#falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffN += 1
					mp += 1
					print("mp")

			rc.writerow([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])

		print("Resultado da rodada: ")
		print([equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm])
		print("Soma 1a parte")
		print(equal+diffP+diffN)
		print("Soma 2a parte")
		print(pp+pr+pm+rp+rr+rm+mp+mr+mm)
		print("Num. Empresas: " + str(QNTD_EMP))
		print("Notas iguais: " + str(equal))
		print("Falsos Positivos: " + str(diffP))
		print("Falsos Negativos: " + str(diffN))

		dadosRodadas.append([equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm])

		if rodadas == 0 :
			maximo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
			minimo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
		elif equal > maximo[0]:
			maximo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
		elif equal < minimo[0]:
			minimo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]

		# plota o gráfico em barras mostrando o número de empresas que deram o mesmo valor (Somatorio e CPeso)
		x = ["Iguais","Falsos Positivos","Falsos Negativos"]
		y = [equal,diffP,diffN]

		for i in range(len(x)):
			plt.text(i, y[i] + 0.1, str(y[i]), ha='center', va='bottom')

		plt.bar(x, y)
		plt.xlabel('Tipos')
		plt.ylabel('Quantidade')
		plt.title('Análise da Precisão')
		plt.show()

	print("Máximo: ")
	print(maximo)
	print("Mínimo: ")
	print(minimo)

	# preparação para os 2 próximos gráficos
	somaPP,somaPR,somaPM,somaRP,somaRR,somaRM,somaMP,somaMR,somaMM = 0,0,0,0,0,0,0,0,0
	for dad in dadosRodadas:
		print(dad)
		somaPP += dad[3]
		somaPR += dad[4]
		somaPM += dad[5]
		somaRP += dad[6]
		somaRR += dad[7]
		somaRM += dad[8]
		somaMP += dad[9]
		somaMR += dad[10]
		somaMM += dad[11]
		print(somaPP,somaPR,somaPM,somaRP,somaRR,somaRM,somaMP,somaMR,somaMM)

	mediaPP = float(somaPP/MAGIC_NUMBER)
	mediaPR = float(somaPR/MAGIC_NUMBER)
	mediaPM = float(somaPM/MAGIC_NUMBER)
	mediaRP = float(somaRP/MAGIC_NUMBER)
	mediaRR = float(somaRR/MAGIC_NUMBER)
	mediaRM = float(somaRM/MAGIC_NUMBER)
	mediaMP = float(somaMP/MAGIC_NUMBER)
	mediaMR = float(somaMR/MAGIC_NUMBER)
	mediaMM = float(somaMM/MAGIC_NUMBER)
	print(mediaPP,mediaPR,mediaPM,mediaRP,mediaRR,mediaRM,mediaMP,mediaMR,mediaMM)
	#'''
	# Matriz de confusão - Média
	matriz_media = np.array([[mediaPP,mediaPR,mediaPM],[mediaRP,mediaRR,mediaRM],[mediaMP,mediaMR,mediaMM]])
	plt.imshow(matriz_media, interpolation='nearest', cmap=plt.cm.Blues)
	plt.title('Matriz de Confusão - Média')
	plt.colorbar()
	tick_marks = np.arange(len(matriz_media))
	plt.xticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	plt.yticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	for i in range(len(matriz_media)):
	    for j in range(len(matriz_media)):
	        plt.text(j, i, str(matriz_media[i][j]), horizontalalignment='center', verticalalignment='center', color='black')
	plt.xlabel('Classe Prevista')
	plt.ylabel('Classe Real')
	plt.show()

	# Matriz de confusão - Melhor caso
	matriz_melhor = np.array([[maximo[3],maximo[4],maximo[5]],[maximo[6],maximo[7],maximo[8]],[maximo[9],maximo[10],maximo[11]]])
	plt.imshow(matriz_melhor, interpolation='nearest', cmap=plt.cm.Blues)
	plt.title('Matriz de Confusão - Melhor caso')
	plt.colorbar()
	tick_marks = np.arange(len(matriz_melhor))
	plt.xticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	plt.yticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	for i in range(len(matriz_melhor)):
	    for j in range(len(matriz_melhor)):
	        plt.text(j, i, str(matriz_melhor[i][j]), horizontalalignment='center', verticalalignment='center', color='black')
	plt.xlabel('Classe Prevista')
	plt.ylabel('Classe Real')
	plt.show()

	# Matriz de confusão - Pior Caso
	matriz_pior = np.array([[minimo[3],minimo[4],minimo[5]],[minimo[6],minimo[7],minimo[8]],[minimo[9],minimo[10],minimo[11]]])
	plt.imshow(matriz_pior, interpolation='nearest', cmap=plt.cm.Blues)
	plt.title('Matriz de Confusão - Pior caso')
	plt.colorbar()
	tick_marks = np.arange(len(matriz_pior))
	plt.xticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	plt.yticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	for i in range(len(matriz_pior)):
	    for j in range(len(matriz_pior)):
	        plt.text(j, i, str(matriz_pior[i][j]), horizontalalignment='center', verticalalignment='center', color='black')
	plt.xlabel('Classe Prevista')
	plt.ylabel('Classe Real')
	plt.show()

	# plota o gráfico de barras de erro

	##### código CHATGPT #####

#'''