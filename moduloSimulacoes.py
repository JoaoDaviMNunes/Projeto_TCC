import sys
import os
import csv
import math
import random
import sqlite3
import moduloDados

paisesLATAM = ["Brasil","Argentina"]
paisesEMEA = ["Alemanha","Reino Unido","França","Inglaterra","Itália","Ucrânia","Holanda"]
paisesAPAC = ["Australia","China","Coréia","India","Japão","Leste Asiático","Russia","Rússia"]
paisesNA = ["Estados Unidos", "Canadá"]
setor = ["setor financeiro","setor de saúde","setor de comércio"]
ataques = ["malware", "ransomware", "phishing", "DDoS"]
local = ["LATAM","NA","APAC","EMEA","América do Sul","América do Norte","Europa","Ásia","Oceania","África","Oriente Médio"]
rodadas = 1000000

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
def montecarlo_simulacao_ataque(rodadas, prob_ataque):
	contadorAtaque = 0
	prob_ataque /= 100

	for _ in range(rodadas):
		if random.random() <= prob_ataque:
			contadorAtaque += 1
	
	probFinal = round(contadorAtaque/rodadas*100,2)
	return probFinal

def simulador_riscos(infoT, infoNT, tudo):
	wait = input("Parada no simulador. Continuar? ")
	#print(tudo)

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

		if ("malware" in info[3] or "ransomware" in info[3]) and tudo[3] == '1':
			#print("==> malware = "+str(info[3])+" = "+str(risco))
			riscoM += risco
			cm += 1
		
		if "phishing" in info[3] and tudo[4] == '1':
			#print("==> phishing = "+str(info[3])+" = "+str(risco))
			riscoP += risco
			cp += 1
		
		if "DDoS" in info[3] and tudo[5] == '1':
			#print("==> DDoS = "+str(info[3])+" = "+str(risco))
			riscoD += risco
			cd += 1

	prob_ataque_malware = montecarlo_simulacao_ataque(rodadas, riscoM/cm if cm else 0)
	prob_ataque_phishing = montecarlo_simulacao_ataque(rodadas, riscoP/cp if cp else 0)
	prob_ataque_ddos = montecarlo_simulacao_ataque(rodadas, riscoD/cd if cd else 0)
	final[0].append(prob_ataque_malware)
	final[0].append(prob_ataque_phishing)
	final[0].append(prob_ataque_ddos)
	if prob_ataque_malware > 0:
		print("A probabilidade de ocorrer um ataque de Malware é de " + str(final[0][0]) + "%")
	if prob_ataque_phishing > 0:
		print("A probabilidade de ocorrer um ataque de Phishing é de " + str(final[0][1]) + "%")
	if prob_ataque_ddos > 0:
		print("A probabilidade de ocorrer um ataque de DDoS é de " + str(final[0][2]) + "%")
	wait = input("Parada. Continuar? ")

	# VERIFICAR O RISCO DE CADA IMPACTO (infoNT)


	# VERIFICAR O RISCO FINANCEIRO (infoT)


	agrupador_informacoes(final)

# ===========================================================================================================
# ANALISADOR DE NEGÓCIOS

# verifica se todas as informações dos campos infoA e infoB são referentes ao que estamos pesquisando
def verifica_utilidade(infoNT, analise):
	for info in infoNT:
		for a in analise:
			if info[3] == a:
				print(info)
	infosCertas = []
	for info in infoNT:
		infoA, infoB = False, False
		for dado in analise:
			if info[3] in dado:
				infoA = True
			if info[4] in dado or info[4] == "-":
				infoB = True
		if infoA and infoB:
			infosCertas.append(info)
	'''for info in infosCertas:
					print(info)'''
	return infosCertas


def analisador_negocios(requisicao):
	print("ENTRANDO - ANALISADOR DE NEGÓCIOS")
	analise, tudo = [], []
	arquivo = list(open(requisicao,"r", encoding="utf-8"))
	tamARQ = len(arquivo)

	for linha in range(tamARQ):
		tudo.extend(arquivo[linha])
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
				analise.append("smishing")
				analise.append("vishing")
			if arquivo[linha][2] == "1":
				analise.append("DDoS")
		elif linha == 2:
			if arquivo[linha][0] == "1":
				analise.append("APAC")
			if arquivo[linha][1] == "1":
				analise.append("LATAM")
			if arquivo[linha][2] == "1":
				analise.append("EMEA")
			if arquivo[linha][3] == "1":
				analise.append("NA")

	while True:
		if '\n' in tudo:
			tudo.remove('\n')
		else:
			break

	# ADICIONA AS PALAVRAS CHAVES DESEJADAS NA LISTA DE DADOS A SEREM COLETADOS NO BANCO DE DADOS
	if tamARQ > 3:
		for i in range(4,tamARQ):
			dadoPesquisa = str(arquivo[i])
			if dadoPesquisa[-1:] == "\n":
				analise.append(dadoPesquisa[:-1])
			else:
				analise.append(dadoPesquisa)

	analise.append("ciberataque")
	print(analise)
	wait = input("Parada no analisador. Continuar? ")
	infoT, infoNT = moduloDados.gerenciadorDados(3,analise,None)
	infoNT = verifica_utilidade(infoNT,analise)
	print("FECHANDO - ANALISADOR DE NEGÓCIOS")
	simulador_riscos(infoT, infoNT, tudo)
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