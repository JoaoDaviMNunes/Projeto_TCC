import random
from random import seed
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics
import math

# definição de variáveis
qntdEmp = 10000
pesoEscolhido = [10,5,8,6,5,10] # rep,per,cob,esc,abr,met
notasPossiveis = ["Ótimo","Bom","Ruim"]

# ================================================================================================
# FUNÇÕES AUXILIARES
# ================================================================================================

# Avalia uma empresa e retorna a nota
def notaEmpresas(total) -> str:
	if total >= 5 :
		nota = "MuitoRelevante"
	elif total >= 3 :
		nota = "Relevante"
	else :
		nota = "PoucoRelevante" 
	#print(str(nota) + "\n")
	return nota

# Calcula qual seria a nota da empresa dada os pesos escolhidos e retorna
def notaEmpresasPeso(lista):
	auxCima = lista[0]*pesoEscolhido[0] + lista[1]*pesoEscolhido[1] + lista[2]*pesoEscolhido[2] + lista[3]*pesoEscolhido[3] + lista[4]*pesoEscolhido[4] + lista[5]*pesoEscolhido[5]
	auxBaixo = pesoEscolhido[0] + pesoEscolhido[1] + pesoEscolhido[2] + pesoEscolhido[3] + pesoEscolhido[4] + pesoEscolhido[5]
	aux = auxCima/auxBaixo*3
	nota = notaEmpresas(aux)
	return nota

# ================================================================================================
# CÓDIGO PRINCIPAL
# ================================================================================================

# Gera valores de empresa randômicos e verifica se são falsos positivos ou negativos
# e armazena numa lista para futuramente plotar
# randomCompanies.csv = [rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso]
with open('randomCompanies.csv', 'w', newline='') as r:
	rc = csv.writer(r) # abre o arquivo para poder escrever
	
	diffP = 0
	diffN = 0
	equal = 0

	falsosP = []
	falsosN = []
	iguais 	= []

	dadosRodadas = []	# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda todos os dados das rodadas
	maximo = []			# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda a rodada com maior precisao
	minimo = []			# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda a rodada com menor precisao

	# gera 10000 empresas randômicas
	for i in range(qntdEmp):
		rep = random.randint(0,2)
		per = random.randint(0,2)
		cob = random.randint(0,2)
		esc = random.randint(0,2)
		abr = random.randint(0,2)
		met = random.randint(0,2)

		somatorio = (rep+per+cob+esc+abr+met)/2
		notaOriginal = notaEmpresas(somatorio)
		notaPeso = notaEmpresasPeso([rep,per,cob,esc,abr,met])

		pp,pr,pm = 0,0,0 # somatorio de transição do estado "PoucoRelevante"
		rp,rr,rm = 0,0,0 # somatorio de transição do estado "Relevante"
		mp,mr,mm = 0,0,0 # somatorio de transição do estado "MuitoRelevante"

		conf = notasPossiveis.index(notaOriginal) - notasPossiveis.index(notaPeso)	# conf = diferença da notaOriginal e da notaPeso
		
		if notaOriginal == "PoucoRelevante":
			if conf == 0:
				iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				equal += 1
				pp += 1
			elif conf == 1:
				falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				diffP += 1
				pr += 1
			elif conf == 2:
				falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				diffP += 1
				pm += 1
		elif notaOriginal == "Relevante":
			if conf == 0:
				iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				equal += 1
				rr += 1
			elif conf == -1:
				falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				diffN +=1
				rp += 1
			elif conf == 1:
				falsosP.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				diffP += 1
				rm += 1
		elif notaOriginal == "MuitoRelevante":
			if conf == 0:
				iguais.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				equal += 1
				mm += 1
			elif conf == -1:
				falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				diffN +=1
				mr += 1
			elif conf == -2:
				falsosN.append([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])
				diffN +=1
				mp += 1

		rc.writerow([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])



	print("Num. Empresas: " + str(qntdEmp))
	print("Notas iguais: " + str(equal))
	print("Falsos Positivos: " + str(diffP))
	print("Falsos Negativos: " + str(diffN))

	for rod in dadosRodadas:
		if equal > rod[0]:
			maximo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
		elif equal < rod[0]:
			minimo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
	dadosRodadas.append([equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm])

	# plota o gráfico em barras
	x = ["Iguais","FalsosP","FalsosN"]
	y = [equal,diffP,diffN]

	plt.bar(x, y)
	plt.xlabel('Tipos')
	plt.ylabel('Quantidade')
	plt.title('Análise da Precisão')
	plt.show()

	# preparação para os 2 próximos gráficos
	somaPP,somaPR,somaPM,somaRP,somaRR,somaRM,somaMP,somaMR,somaMM = 0,0,0,0,0,0,0,0,0
	for dad in dadosRodadas:
		somaPP += dad[3]
		somaPR += dad[4]
		somaPM += dad[5]
		somaRP += dad[6]
		somaRR += dad[7]
		somaRM += dad[8]
		somaMP += dad[9]
		somaMR += dad[10]
		somaMM += dad[11]

	mediaPP = somaPP/qntdEmp
	mediaPR = somaPR/qntdEmp
	mediaPM = somaPM/qntdEmp
	mediaRP = somaRP/qntdEmp
	mediaRR = somaRR/qntdEmp
	mediaRM = somaRM/qntdEmp
	mediaMP = somaMP/qntdEmp
	mediaMR = somaMR/qntdEmp
	mediaMM = somaMM/qntdEmp
	# plota o gráfico em matriz de confusão

	##### código CHATGPT #####


	# plota o gráfico de barras de erro

	##### código CHATGPT #####

