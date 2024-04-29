import sys
import os
import csv
import math
import random
import sqlite3
import moduloDados

setor = ["setor financeiro","setor de saúde","setor de comércio"]
ataques = ["malware", "ransomware", "phishing", "DDoS"]
local = ["América do Sul","região: LAC","América do Norte","região: NA","Europa","região: EMEA","Ásia","região: APAC","Oceania","região: APAC","África","região: EMEA"]

# ===========================================================================================================
# GERADOR DE RELATÓRIOS
# Recebe, condensa, organiza e formata as informações, de forma a gerar um relatório completo para o usuário.
# Este relatório dispõe de uma análise da empresa (informada na requisição do usuário), como sua estimativa de tamanho, porte econômico e ativos importantes. 
# Este documento igualmente contém o risco da empresa de sofrer um ciberataque de Malware, Phishing e DDoS, com base nas simulações realizadas previamente.

def gerador_relatorios():
	saida = open("relatorio.pdf", "w")

	# ...
	
	saida.close()

# ===========================================================================================================
# AGRUPADOR DE INFORMAÇÕES
# solicitar ao Gerenciador de Dados as informações relevantes à requisição e informar com precisão quais informações dessas são redirecionadas

def agrupador_informacoes(info):
	gerador_relatorios()

# ===========================================================================================================
# SIMULADOR DE RISCOS
def simulador_riscos(infoT, infoNT):
	wait = input("Parada no simulador. Continuar? ")

	final = [[],[]]
	riscoM, riscoP, riscoD = 0,0,0	# contator total das porcentagens de cada ataque
	cm, cp, cd = 0,0,0				# contador de itens de cada ataque

	# VERIFICAR O RISCO DA EMPRESA SOFRER O RISCO DO ATAQUE (infoNT)
	#print(infoNT)
	for info in infoNT:
		#print(info[3])
		
		risco = 0
		if info[5] != "-":
			risco = float(info[5])
		else:
			risco = float(info[6])

		if "malware" in info[3] or "ransomware" in info[3]:
			print("==> malware = "+str(info[3])+" = "+str(risco))
			riscoM += risco
			cm += 1
		
		if "phishing" in info[3]:
			print("==> phishing = "+str(info[3])+" = "+str(risco))
			riscoP += risco
			cp += 1
		
		if "DDoS" in info[3]:
			print("==> DDoS = "+str(info[3])+" = "+str(risco))
			riscoD += risco
			cd += 1

	final[0].append(round((riscoM/cm),2) if cm else 0)
	final[0].append(round((riscoP/cp),2) if cp else 0)
	final[0].append(round((riscoD/cd),2) if cd else 0)
	print("A probabilidade de ocorrer um ataque de Malware é de " + str(final[0][0]) + "%")
	print("A probabilidade de ocorrer um ataque de Phishing é de " + str(final[0][1]) + "%")
	print("A probabilidade de ocorrer um ataque de DDoS é de " + str(final[0][2]) + "%")
	wait = input("Parada. Continuar? ")

	# VERIFICAR O RISCO DE CADA IMPACTO (infoNT)


	# VERIFICAR O RISCO FINANCEIRO (infoT)


	agrupador_informacoes(final)

# ===========================================================================================================
# ANALISADOR DE NEGÓCIOS

def analisador_negocios(requisicao):
	print("ENTRANDO - ANALISADOR DE NEGÓCIOS")
	analise = []
	arquivo = list(open(requisicao,"r", encoding="utf-8"))
	tamARQ = len(arquivo)

	for linha in range(tamARQ):
		if linha == 0:
			if arquivo[linha][0] == "1":
				analise.append("setor financeiro")
			if arquivo[linha][1] == "1":
				analise.append("setor de saúde")
			if arquivo[linha][2] == "1":
				analise.append("setor de comércio")
		elif linha == 1:
			if arquivo[linha][0] == "1":
				analise.append("malware")
				analise.append("ransomware")
			if arquivo[linha][1] == "1":
				analise.append("phishing")
			if arquivo[linha][2] == "1":
				analise.append("DDoS")
		elif linha == 2:
			if arquivo[linha][0] == "1":
				analise.append("América do Sul")
				analise.append("região: LAC")
			if arquivo[linha][1] == "1":
				analise.append("América do Norte")
				analise.append("região: NA")
			if arquivo[linha][2] == "1":
				analise.append("Europa")
				analise.append("região: EMEA")
			if arquivo[linha][3] == "1":
				analise.append("Ásia")
				analise.append("região: APAC")
			if arquivo[linha][4] == "1":
				analise.append("Oceania")
				analise.append("região: APAC")
			if arquivo[linha][5] == "1":
				analise.append("África")
				analise.append("região: EMEA")

	# ADICIONA AS PALAVRAS CHAVES DESEJADAS NA LISTA DE DADOS A SEREM COLETADOS NO BANCO DE DADOS
	if tamARQ > 3:
		for i in range(4,tamARQ):
			dadoPesquisa = str(arquivo[i])
			if dadoPesquisa[-1:] == "\n":
				analise.append(dadoPesquisa[:-1])
			else:
				analise.append(dadoPesquisa)

	print(analise)
	wait = input("Parada no analisador. Continuar? ")
	infoT, infoNT = moduloDados.gerenciadorDados(3,analise,None)
	print("FECHANDO - ANALISADOR DE NEGÓCIOS")
	simulador_riscos(infoT, infoNT)
	pass

# ===========================================================================================================

def main():
	requisicao = sys.argv[1]
	if os.path.exists(requisicao):
		analisador_negocios(requisicao)
	else:
		print("O arquivo "+requisicao+" não existe no diretório")
	print("Arquivo de saída gerado!")

if __name__ == "__main__":
	main()