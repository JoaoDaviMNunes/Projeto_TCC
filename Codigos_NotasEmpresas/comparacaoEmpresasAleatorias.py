import os
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
MAGIC_NUMBER = 30
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
	maximo = []			# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda a rodada com maior precisao
	minimo = []			# [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm], guarda a rodada com menor precisao

	for rodadas in range(MAGIC_NUMBER):
		diffP = 0
		diffN = 0
		equal = 0

		pp,pr,pm = 0,0,0 # somatorio de transição do estado "PoucoRelevante"
		rp,rr,rm = 0,0,0 # somatorio de transição do estado "Relevante"
		mp,mr,mm = 0,0,0 # somatorio de transição do estado "MuitoRelevante"

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
			if notaOriginal == "PoucoRelevante":
				if conf == 0:		# PoucoRelevante -> PoucoRelevante
					equal += 1
					pp += 1
				elif conf == 1:		# PoucoRelevante -> Relevante
					diffP += 1
					pr += 1
				elif conf == 2:		# PoucoRelevante -> MuitoRelevante
					diffP += 1
					pm += 1
			elif notaOriginal == "Relevante":
				if conf == 0:		# Relevante -> Relevante
					equal += 1
					rr += 1
				elif conf == -1:	# Relevante -> PoucoRelevante
					diffN += 1
					rp += 1
				elif conf == 1:		# Relevante -> MuitoRelevante
					diffP += 1
					rm += 1
			elif notaOriginal == "MuitoRelevante":
				if conf == 0:		# MuitoRelevante -> MuitoRelevante
					equal += 1
					mm += 1
				elif conf == -1:	# MuitoRelevante -> Relevante
					diffN += 1
					mr += 1
				elif conf == -2:	# MuitoRelevante -> PoucoRelevante
					diffN += 1
					mp += 1

			rc.writerow([rep,per,cob,esc,abr,met,somatorio,notaOriginal,notaPeso])

		soma1aparte = equal+diffP+diffN
		soma2aparte = pp+pr+pm+rp+rr+rm+mp+mr+mm
		if soma1aparte != QNTD_EMP:
			print("Soma 1a parte" + str(soma1aparte))
		elif soma2aparte != QNTD_EMP:
			print("Soma 2a parte" + str(soma2aparte))

		dadosRodadas.append([equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm])
		#print([equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm])


		# MÍNIMO = é a rodada que possui o menor número de empresas que mantiveram os mesmos scores após a aplicação dos pesos
		# MÁXIMO = é a rodada que possui o maior número de empresas que mantiveram os mesmos scores após a aplicação dos pesos
		if rodadas == 0 :
			maximo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
			minimo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
		elif equal > maximo[0]:
			maximo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]
		elif equal < minimo[0]:
			minimo = [equal,diffP,diffN,pp,pr,pm,rp,rr,rm,mp,mr,mm]

	
	#print("Máximo: ")
	#print(maximo)
	#print("Mínimo: ")
	#print(minimo)

	# preparação para os próximos gráficos
	somaEQ,somaDP,somaDN = 0,0,0
	somaPP,somaPR,somaPM = 0,0,0
	somaRP,somaRR,somaRM = 0,0,0
	somaMP,somaMR,somaMM = 0,0,0
	for dad in dadosRodadas:
		somaEQ += dad[0]
		somaDP += dad[1]
		somaDN += dad[2]
		somaPP += dad[3]
		somaPR += dad[4]
		somaPM += dad[5]
		somaRP += dad[6]
		somaRR += dad[7]
		somaRM += dad[8]
		somaMP += dad[9]
		somaMR += dad[10]
		somaMM += dad[11]

	mediaEQ = round(float(somaEQ/MAGIC_NUMBER),2)
	mediaDP = round(float(somaDP/MAGIC_NUMBER),2)
	mediaDN = round(float(somaDN/MAGIC_NUMBER),2)
	mediaPP = round(float(somaPP/MAGIC_NUMBER),2)
	mediaPR = round(float(somaPR/MAGIC_NUMBER),2)
	mediaPM = round(float(somaPM/MAGIC_NUMBER),2)
	mediaRP = round(float(somaRP/MAGIC_NUMBER),2)
	mediaRR = round(float(somaRR/MAGIC_NUMBER),2)
	mediaRM = round(float(somaRM/MAGIC_NUMBER),2)
	mediaMP = round(float(somaMP/MAGIC_NUMBER),2)
	mediaMR = round(float(somaMR/MAGIC_NUMBER),2)
	mediaMM = round(float(somaMM/MAGIC_NUMBER),2)
	#print("Média: ")
	#print([mediaEQ,mediaDP,mediaDN,mediaPP,mediaPR,mediaPM,mediaRP,mediaRR,mediaRM,mediaMP,mediaMR,mediaMM])
	#print(str(mediaEQ+mediaDP+mediaDN) + " | " + str(mediaPP+mediaPR+mediaPM+mediaRP+mediaRR+mediaRM+mediaMP+mediaMR+mediaMM))

	# Gráfico de Barras - Quantidade de Empresas (em porcentagem)
	x = ["PoucoRelevante","Relevante","MuitoRelevante"]
	y = [round((mediaPP+mediaPR+mediaPM)/QNTD_EMP*100,2),round((mediaRR+mediaRP+mediaRM)/QNTD_EMP*100,2),round((mediaMM+mediaMR+mediaMP)/QNTD_EMP*100,2)]
	for i in range(len(x)):
		plt.text(i, y[i] + 0.1, str(y[i]), ha='center', va='bottom')
	plt.bar(x, y)
	plt.xlabel('Notas')
	plt.ylabel('Porcentagem')
	plt.title('Quantidade de Empresas')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'1PorcentagemEmpresas.png'))
	plt.show()

	# Gráfico de Barras - Quantidade de Empresas (em número)
	x = ["PoucoRelevante","Relevante","MuitoRelevante"]
	y = [round(mediaPP+mediaPR+mediaPM,2),round(mediaRR+mediaRP+mediaRM,2),round(mediaMM+mediaMR+mediaMP,2)]
	for i in range(len(x)):
		plt.text(i, y[i] + 0.1, str(y[i]), ha='center', va='bottom')
	plt.bar(x, y)
	plt.xlabel('Notas')
	plt.ylabel('Quantidade')
	plt.title('Número de Empresas')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'2NumeroEmpresas.png'))
	plt.show()

	# Gráfico de Barras - Quantidade de Notas (em número)
	x = ["PP","PR","PM","RP","RR","RM","MP","MR","MM"]
	y = [round(mediaPP,2),round(mediaPR,2),round(mediaPM,2),round(mediaRP,2),round(mediaRR,2),round(mediaRM,2),round(mediaMP,2),round(mediaMR,2),round(mediaMM,2)]
	for i in range(len(x)):
		plt.text(i, y[i] + 0.1, str(y[i]), ha='center', va='bottom')
	plt.bar(x, y)
	plt.xlabel('Notas')
	plt.ylabel('Quantidade')
	plt.title('Média de Notas e Transições')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'3NumeroNotas.png'))
	plt.show()

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
	plt.xlabel('Nota - Com Pesos')
	plt.ylabel('Nota - Somatório')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'4MatConfMedia.png'))
	plt.show()

	# Matriz de confusão - Média (em porcentagem)
	matriz_media = np.array([[round(mediaPP/QNTD_EMP*100,2),round(mediaPR/QNTD_EMP*100,2),round(mediaPM/QNTD_EMP*100,2)],[round(mediaRP/QNTD_EMP*100,2),round(mediaRR/QNTD_EMP*100,2),round(mediaRM/QNTD_EMP*100,2)],[round(mediaMP/QNTD_EMP*100,2),round(mediaMR/QNTD_EMP*100,2),round(mediaMM/QNTD_EMP*100,2)]])
	plt.imshow(matriz_media, interpolation='nearest', cmap=plt.cm.Blues)
	plt.title('Matriz de Confusão - Média (Em Porcentagem)')
	plt.colorbar()
	tick_marks = np.arange(len(matriz_media))
	plt.xticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	plt.yticks(tick_marks, ['PoucoRelevante', 'Relevante', 'MuitoRelevante'])
	for i in range(len(matriz_media)):
	    for j in range(len(matriz_media)):
	        plt.text(j, i, str(matriz_media[i][j]), horizontalalignment='center', verticalalignment='center', color='black')
	plt.xlabel('Nota - Com Pesos')
	plt.ylabel('Nota - Somatório')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'5MatConfMediaPorc.png'))
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
	plt.xlabel('Nota - Com Pesos')
	plt.ylabel('Nota - Somatório')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'6MatConfMelhor.png'))
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
	plt.xlabel('Nota - Com Pesos')
	plt.ylabel('Nota - Somatório')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'7MatConfPior.png'))
	plt.show()

	# Gráfico em barras de erros (CHATGPT)
	matriz_bar = np.array([[minimo[3],mediaPP,maximo[3]],[minimo[7],mediaRR,maximo[7]],[minimo[11],mediaMM,maximo[11]]])
	minimos = np.min(matriz_bar, axis=1)
	medias = np.mean(matriz_bar, axis=1)
	maximos = np.max(matriz_bar, axis=1)
	erros_inferiores = [abs(mediaPP-minimo[3]),abs(mediaRR-minimo[7]),abs(mediaMM-minimo[11])]
	erros_superiores = [abs(maximo[3]-mediaPP),abs(maximo[7]-mediaRR),abs(maximo[11]-mediaMM)]
	erros = [erros_inferiores, erros_superiores]
	labels = ['PoucoRelevante', 'Relevante', 'MuitoRelevante']
	x = np.arange(len(labels))
	largura_barra = 0.35
	fig, ax = plt.subplots()
	barras = ax.bar(x, medias, largura_barra, yerr=erros, label='Empresas', capsize=2)
	ax.set_xlabel('Notas')
	ax.set_ylabel('Quantidade')
	ax.set_title('Gráfico de Barras de Erro')
	ax.set_xticks(x)
	ax.set_xticklabels(labels)
	ax.legend()
	for i in range(len(barras)):
	    yval = barras[i].get_height()
	    yerr_lower = erros_inferiores[i]
	    yerr_upper = erros_superiores[i]
	    ax.text(barras[i].get_x() + barras[i].get_width() / 2., yval,
	            f'{yval:.2f}\n({yerr_lower:.2f}, {yerr_upper:.2f})',
	            ha='center', va='bottom')
	plt.tight_layout()
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'8BarErrNotas.png'))
	plt.show()

	# Gráfico de Barras - Quantidade de Notas (em número)
	x = ["Iguais","Falsos Positivos","Falsos Negativos"]
	y = [round(mediaEQ,2),round(mediaDP,2),round(mediaDN,2)]
	for i in range(len(x)):
		plt.text(i, y[i] + 0.1, str(y[i]), ha='center', va='bottom')
	plt.bar(x, y)
	plt.xlabel('Avaliação')
	plt.ylabel('Quantidade')
	plt.title('Análise de Transição')
	caminho_pasta = "./Imagens"
	os.makedirs(caminho_pasta, exist_ok=True)
	plt.savefig(os.path.join(caminho_pasta,'9AnaliseTransicao.png'))
	plt.show()