import random
from random import seed
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics
import math
from scipy import stats
from collections import Counter

# inicializações
pes00,pes01,pes02,pes03,pes04,pes05,pes06,pes07,pes08,pes09,pes010 = 0,0,0,0,0,0,0,0,0,0,0
pes10,pes11,pes12,pes13,pes14,pes15,pes16,pes17,pes18,pes19,pes110 = 0,0,0,0,0,0,0,0,0,0,0
pes20,pes21,pes22,pes23,pes24,pes25,pes26,pes27,pes28,pes29,pes210 = 0,0,0,0,0,0,0,0,0,0,0
pes30,pes31,pes32,pes33,pes34,pes35,pes36,pes37,pes38,pes39,pes310 = 0,0,0,0,0,0,0,0,0,0,0
pes40,pes41,pes42,pes43,pes44,pes45,pes46,pes47,pes48,pes49,pes410 = 0,0,0,0,0,0,0,0,0,0,0
pes50,pes51,pes52,pes53,pes54,pes55,pes56,pes57,pes58,pes59,pes510 = 0,0,0,0,0,0,0,0,0,0,0

# ===========================================================================
# Função principal
# Entrada:
# pesosReports.csv = [p1,p2,p3,p4,p5,p6,precisao]
# Saída: 
# contagemPesos.csv = 
with open('pesosReports.csv') as p, open ('contagemPesos.csv', 'w', newline='') as c:
	# abrindo os arquivos, um para ler os dados, outro para guardar as informações
	pesos = csv.reader(p, delimiter=',')
	cp = csv.writer(c)

	# inicializando o contador de linhas
	totalLinhas = 0
	totalPrecisao70 = 0
	totalPrecisao75 = 0
	totalPrecisao80 = 0
	totalPrecisao85 = 0
	totalPrecisao90 = 0
	totalPrecisao95 = 0
	totalPrecisao100 = 0

	for linha in pesos:
		# ignora a primeira linha, que descreve o que são as colunas (arquivo de entrada)
		if totalLinhas != 0:
			#verifica se a precisão foi de 95% e soma no contador
			if float(linha[6]) == 70.0:
				totalPrecisao70 += 1
			elif float(linha[6]) == 75.0:
				totalPrecisao75 += 1
			elif float(linha[6]) == 80.0:
				totalPrecisao80 += 1
			elif float(linha[6]) == 85.0:
				totalPrecisao85 += 1
			elif float(linha[6]) == 90.0:
				totalPrecisao90 += 1
			elif float(linha[6]) == 95.0:
				totalPrecisao95 += 1
			elif float(linha[6]) == 100.0:
				totalPrecisao100 += 1

			match int(linha[0]):
				case 0:
					pes00 += 1
				case 1:
					pes01 += 1
				case 2:
					pes02 += 1
				case 3:
					pes03 += 1
				case 4:
					pes04 += 1
				case 5:
					pes05 += 1
				case 6:
					pes06 += 1
				case 7:
					pes07 += 1
				case 8:
					pes08 += 1
				case 9:
					pes09 += 1
				case 10:
					pes010 += 1

			match int(linha[1]):
				case 0:
					pes10 += 1
				case 1:
					pes11 += 1
				case 2:
					pes12 += 1
				case 3:
					pes13 += 1
				case 4:
					pes14 += 1
				case 5:
					pes15 += 1
				case 6:
					pes16 += 1
				case 7:
					pes17 += 1
				case 8:
					pes18 += 1
				case 9:
					pes19 += 1
				case 10:
					pes110 += 1

			match int(linha[2]):
				case 0:
					pes20 += 1
				case 1:
					pes21 += 1
				case 2:
					pes22 += 1
				case 3:
					pes23 += 1
				case 4:
					pes24 += 1
				case 5:
					pes25 += 1
				case 6:
					pes26 += 1
				case 7:
					pes27 += 1
				case 8:
					pes28 += 1
				case 9:
					pes29 += 1
				case 10:
					pes210 += 1

			match int(linha[3]):
				case 0:
					pes30 += 1
				case 1:
					pes31 += 1
				case 2:
					pes32 += 1
				case 3:
					pes33 += 1
				case 4:
					pes34 += 1
				case 5:
					pes35 += 1
				case 6:
					pes36 += 1
				case 7:
					pes37 += 1
				case 8:
					pes38 += 1
				case 9:
					pes39 += 1
				case 10:
					pes310 += 1

			match int(linha[4]):
				case 0:
					pes40 += 1
				case 1:
					pes41 += 1
				case 2:
					pes42 += 1
				case 3:
					pes43 += 1
				case 4:
					pes44 += 1
				case 5:
					pes45 += 1
				case 6:
					pes46 += 1
				case 7:
					pes47 += 1
				case 8:
					pes48 += 1
				case 9:
					pes49 += 1
				case 10:
					pes410 += 1

			match int(linha[5]):
				case 0:
					pes50 += 1
				case 1:
					pes51 += 1
				case 2:
					pes52 += 1
				case 3:
					pes53 += 1
				case 4:
					pes54 += 1
				case 5:
					pes55 += 1
				case 6:
					pes56 += 1
				case 7:
					pes57 += 1
				case 8:
					pes58 += 1
				case 9:
					pes59 += 1
				case 10:
					pes510 += 1


		totalLinhas += 1

	cp.writerow([pes00,pes01,pes02,pes03,pes04,pes05,pes06,pes07,pes08,pes09,pes010])
	cp.writerow([pes10,pes11,pes12,pes13,pes14,pes15,pes16,pes17,pes18,pes19,pes110])
	cp.writerow([pes20,pes21,pes22,pes23,pes24,pes25,pes26,pes27,pes28,pes29,pes210])
	cp.writerow([pes30,pes31,pes32,pes33,pes34,pes35,pes36,pes37,pes38,pes39,pes310])
	cp.writerow([pes40,pes41,pes42,pes43,pes44,pes45,pes46,pes47,pes48,pes49,pes410])
	cp.writerow([pes50,pes51,pes52,pes53,pes54,pes55,pes56,pes57,pes58,pes59,pes510])
	print("Total de " + str(totalLinhas) + " linhas lidas no arquivo de entrada.")

	# Gráfico em barras - Quantidade de conjunto de pesos com X% de precisão
	x = ["70%","75%","80%","85%","90%","95%","100%"]
	y = [totalPrecisao70,totalPrecisao75,totalPrecisao80,totalPrecisao85,totalPrecisao90,totalPrecisao95,totalPrecisao100]
	for i in range(len(x)):
		plt.text(i, y[i] + 0.1, str(y[i]), ha='center', va='bottom')
	plt.bar(x, y)
	plt.xlabel('Precisões')
	plt.ylabel('Quantidade')
	plt.title('Análise da Precisão')
	plt.show()

'''
# abrindo o arquivo de contagem e analisando estaticamente
with open ('contagemPesos.csv') as c:
	entrada = csv.reader(c, delimiter=',')
	cp = []

	for linha in entrada:
		cp.append(linha)

	media0 = statistics.mean(cp[0])
	mediana0 = statistics.median(cp[0])
	moda0 = statistics.mode(cp[0])
	media1 = statistics.mean(cp[1])
	mediana1 = statistics.median(cp[1])
	moda1 = statistics.mode(cp[1])
	media2 = statistics.mean(cp[2])
	mediana2 = statistics.median(cp[2])
	moda2 = statistics.mode(cp[2])
	media3 = statistics.mean(cp[3])
	mediana3 = statistics.median(cp[3])
	moda3 = statistics.mode(cp[3])
	media4 = statistics.mean(cp[4])
	mediana4 = statistics.median(cp[4])
	moda4 = statistics.mode(cp[4])
	media5 = statistics.mean(cp[5])
	mediana5 = statistics.median(cp[5])
	moda5 = statistics.mode(cp[5])

	print("Media coluna0:" + str(media0))
	print("Mediana coluna0:" + str(mediana0))
	print("Moda coluna0:" + str(moda0))
	print("Media coluna1:" + str(media1))
	print("Mediana coluna1:" + str(mediana1))
	print("Moda coluna1:" + str(moda1))
	print("Media coluna2:" + str(media2))
	print("Mediana coluna2:" + str(mediana2))
	print("Moda coluna2:" + str(moda2))
	print("Media coluna3:" + str(media3))
	print("Mediana coluna3:" + str(mediana3))
	print("Moda coluna3:" + str(moda3))
	print("Media coluna4:" + str(media4))
	print("Mediana coluna4:" + str(mediana4))
	print("Moda coluna4:" + str(moda4))
	print("Media coluna5:" + str(media5))
	print("Mediana coluna5:" + str(mediana5))
	print("Moda coluna5:" + str(moda5))
'''
# ===========================================================================