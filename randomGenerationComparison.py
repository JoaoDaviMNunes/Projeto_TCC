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
MAGIC_NUMBER = 1
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

			conf = notasPossiveis.index(notaOriginal) - notasPossiveis.index(notaPeso)
			
			if notaOriginal == "PoucoRelevante":
				if conf == 0:
					#iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					print(pp)
					equal += 1
					pp += 1
				elif conf == 1:
					#falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffP += 1
					pr += 1
					print(pr)
				elif conf == 2:
					#falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffP += 1
					pm += 1
					print(pm)
			elif notaOriginal == "Relevante":
				if conf == 0:
					#iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					equal += 1
					rr += 1
					print(rr)
				elif conf == -1:
					#falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffN += 1
					rp += 1
					print(rp)
				elif conf == 1:
					#falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffP += 1
					rm += 1
					print(rm)
			elif notaOriginal == "MuitoRelevante":
				if conf == 0:
					#iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					equal += 1
					mm += 1
					print(mm)
				elif conf == -1:
					#falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffN += 1
					mr += 1
					print(mr)
				elif conf == -2:
					#falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
					diffN += 1
					mp += 1
					print(mp)

			print([equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm])
			rc.writerow([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])

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
	#--- plota o gráfico em matriz de confusão
	matriz_real = np.array([[mediaPP,mediaPR,mediaPM],[mediaRP,mediaRR,mediaRM],[mediaMP,mediaMR,mediaRM]])

	# ['Classe 0', 'Classe 1', 'Classe 2'] = ['PoucoRelevante', 'Relevante', 'MuitoRelevante']
	#sns.heatmap(matriz_real, annot=True, fmt='f', cmap='Blues', xticklabels=['PoucoRelevante', 'Relevante', 'MuitoRelevante'], yticklabels=['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	#plt.xlabel('Classe Prevista')
	#plt.ylabel('Classe Real')
	#plt.title('Matriz de Confusão')
	#plt.show()

	# Plotagem da matriz de confusão
	plt.imshow(matriz_real, interpolation='nearest', cmap=plt.cm.Blues)
	plt.title('Matriz de Confusão')
	plt.colorbar()

	# Rotulação dos eixos
	tick_marks = np.arange(len(matriz_real))
	plt.xticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	plt.yticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])

	# Adiciona os valores de cada célula
	for i in range(len(matriz_real)):
	    for j in range(len(matriz_real)):
	        plt.text(j, i, str(matriz_real[i][j]), horizontalalignment='center', verticalalignment='center', color='black')

	plt.xlabel('Classe Prevista')
	plt.ylabel('Classe Real')
	plt.show()


	# plota o gráfico de barras de erro

	##### código CHATGPT #####

#'''