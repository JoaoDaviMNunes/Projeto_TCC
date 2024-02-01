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

# Avalia uma empresa e retorna a nota dela
def notaEmpresas(total) -> str:
	if total >= 5 :
		nota = "Ótimo" # Muito Relevante
	elif total >= 3 :
		nota = "Bom" # Relevante
	else :
		nota = "Ruim" # Pouco Relevante
	#print(str(nota) + "\n")
	return nota

# Calcula qual seria a nota da empresa dada os pesos escolhidos e retorna
def notaEmpresasPeso(lista,notaOriginal):
	auxCima = lista[0]*pesoEscolhido[0] + lista[1]*pesoEscolhido[1] + lista[2]*pesoEscolhido[2] + lista[3]*pesoEscolhido[3] + lista[4]*pesoEscolhido[4] + lista[5]*pesoEscolhido[5]
	auxBaixo = pesoEscolhido[0] + pesoEscolhido[1] + pesoEscolhido[2] + pesoEscolhido[3] + pesoEscolhido[4] + pesoEscolhido[5]
	aux = auxCima/auxBaixo*3
	#print(lista)
	#print(aux)
	#print(notaOriginal)
	nota = notaEmpresas(aux)
	return nota

# ================================================================================================
# CÓDIGO PRINCIPAL
# ================================================================================================

# Lê 
with open('randomCompanies.csv', 'w', newline='') as r:
	rc = csv.writer(r) # abre o arquivo para poder escrever
	
	diffP = 0
	diffN = 0
	equal = 0

	falsosP = []
	falsosN = []

	# gera 10000 empresas randômicas
	for _ in range(qntdEmp):
		rep = random.randint(0,2)
		per = random.randint(0,2)
		cob = random.randint(0,2)
		esc = random.randint(0,2)
		abr = random.randint(0,2)
		met = random.randint(0,2)

		notaSoma = (rep+per+cob+esc+abr+met)/2
		nota = notaEmpresas(notaSoma)
		notaPeso = notaEmpresasPeso([rep,per,cob,esc,abr,met],nota)

		if notasPossiveis.index(nota) < notasPossiveis.index(notaPeso):
			falsosP.append([rep,per,cob,esc,abr,met,notaSoma,nota,notaPeso])
			diffP += 1
		elif notasPossiveis.index(nota) > notasPossiveis.index(notaPeso):
			falsosN.append([rep,per,cob,esc,abr,met,notaSoma,nota,notaPeso])
			diffN +=1
		elif notasPossiveis.index(nota) == notasPossiveis.index(notaPeso):
			equal += 1

		# plota
		plt.xlabel("Números de cada tipo")
		plt.plot([equal,diffP,diffN],[0,3500,7000])
		plt.show()

		rc.writerow([rep,per,cob,esc,abr,met,notaSoma,nota,notaPeso])

	total = equal+diffN+diffP
	print("Notas iguais: " + str(equal) + " (" + str(equal/total*100) + ")")
	print("Falsos Positivos: " + str(diffP) + " (" + str(diffP/total*100) + ")")
	print("Falsos Negativos: " + str(diffN) + " (" + str(diffN/total*100) + ")")