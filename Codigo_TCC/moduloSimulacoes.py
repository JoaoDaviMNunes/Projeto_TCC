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
def montecarlo_simulacao_ataque(rodadas, prob_ataque, prob_impactos):
	contadorAtaque = 0
	contadorImpacto = [0,0,0,0,0]
	prob_ataque /= 100

	for _ in range(rodadas):
		if random.random() <= prob_ataque:
			contadorAtaque += 1
			if random.random() <= prob_impactos[0]: # vazamento de dados (malware e phishing)
				contadorImpacto[0] += 1
			if random.random() <= prob_impactos[1]: # dados criptografados (malware)
				contadorImpacto[1] += 1
			if random.random() <= prob_impactos[2]: # perda de desempenho (malware, phishing e DDoS)
				contadorImpacto[2] += 1
			if random.random() <= prob_impactos[3]: # indisponibilidade do sistema (malware e DDoS)
				contadorImpacto[3] += 1
			if random.random() <= prob_impactos[4]: # roubo de credenciais (phishing)
				contadorImpacto[4] += 1
	
	print("contador ataque: " + str(contadorAtaque))
	probFinalAtaque = round(contadorAtaque/rodadas*100,2)
	probFinalVaz = round(contadorImpacto[0]/contadorAtaque*100,2)
	probFinalCrip = round(contadorImpacto[1]/contadorAtaque*100,2)
	probFinalDes = round(contadorImpacto[2]/contadorAtaque*100,2)
	probFinalInd = round(contadorImpacto[3]/contadorAtaque*100,2)
	probFinalCred = round(contadorImpacto[4]/contadorAtaque*100,2)
	return probFinalAtaque, [probFinalVaz, probFinalVaz, probFinalCrip, probFinalDes, probFinalInd, probFinalCred]

def simulador_riscos(infoT, infoNT, tudo):
	wait = input("Parada no simulador. Continuar? ")
	#print(tudo)

	final = []
	riscoM, riscoP, riscoD = 0,0,0	# contator total das porcentagens de cada ataque
	impVaz, impCrip, impDes, impInd, impCred = 0,0,0,0,0 # contador total das porcentagens de sucesso de cada impacto
	cm, cp, cd = 0,0,0				# contador de itens de cada ataque
	contVaz, contCrip, contDes, contInd, contCred = 0,0,0,0,0
	probM_impactos, probP_impactos, probD_impactos = 0,0,0

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
		
		if "vazamento de dados" in info[3]:
			impVaz +=1
			contVaz += risco
		if "dados criptografados" in info[3]:
			impCrip += 1
			contCrip += risco
		if "perda de desempenho" in info[3]:
			impDes += 1
			contDes += risco
		if "indisponibilidade do sistema" in info[3]:
			impInd += 1
			contInd += risco
		if "roubo de credenciais" in info[3]:
			impCred += 1
			contCred += risco

	prob_impactos = [contVaz/impVaz if impVaz else 0, contCrip/impCrip if impCrip else 0, contDes/impDes if impDes else 0, contInd/impInd if impInd else 0, contCred/impCred if impCred else 0]
	print("IMPACTOS")
	print(prob_impactos)


	if cm > 0:
		prob_ataque_malware, probM_impactos = montecarlo_simulacao_ataque(rodadas, riscoM/cm, prob_impactos)
	if cp > 0:
		prob_ataque_phishing, probP_impactos = montecarlo_simulacao_ataque(rodadas, riscoP/cp, prob_impactos)
	if cd > 0:
		prob_ataque_ddos, probD_impactos = montecarlo_simulacao_ataque(rodadas, riscoD/cd, prob_impactos)
	final.append([prob_ataque_malware, probM_impactos])
	final.append([prob_ataque_phishing, probP_impactos])
	final.append([prob_ataque_ddos, probD_impactos])
	if prob_ataque_malware > 0:
		print("A probabilidade de ocorrer um ataque de Malware é de " + str(final[0][0]) + "%")
		print("Dado que é malware, a probabilidade de ocorrer vazamento de dados é de " + str(final[0][1][0]) + "%")
		print("Dado que é malware, a probabilidade de ocorrer dados criptografados é de " + str(final[0][1][1]) + "%")
		print("Dado que é malware, a probabilidade de ocorrer perda de desempenho é de " + str(final[0][1][2]) + "%")
		print("Dado que é malware, a probabilidade de ocorrer indisponibilidade do sistema é de " + str(final[0][1][3]) + "%")
	if prob_ataque_phishing > 0:
		print("A probabilidade de ocorrer um ataque de Phishing é de " + str(final[1][0]) + "%")
		print("Dado que é phishing, a probabilidade de ocorrer vazamento de dados é de " + str(final[1][1][0]) + "%")
		print("Dado que é phishing, a probabilidade de ocorrer perda de desempenho é de " + str(final[1][1][2]) + "%")
		print("Dado que é phishing, a probabilidade de ocorrer roubo de credenciais é de " + str(final[1][1][4]) + "%")
	if prob_ataque_ddos > 0:
		print("A probabilidade de ocorrer um ataque de DDoS é de " + str(final[2][0]) + "%" + "%")
		print("Dado que é DDoS, a probabilidade de ocorrer perda de desempenho é de " + str(final[2][1][2]) + "%")
		print("Dado que é DDoS, a probabilidade de ocorrer indisponibilidade do sistema é de " + str(final[2][1][3]) + "%")
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

	# verifica de acordo com o ataque e adiciona os impactos
	for dado in analise:
		if dado == "malware":
			if "vazamento de dados" not in analise:
				analise.append("vazamento de dados")
			if "dados criptografados" not in analise:
				analise.append("dados criptografados")
			if "perda de desempenho" not in analise:
				analise.append("perda de desempenho")
			if "indisponibilidade do sistema" not in analise:
				analise.append("indisponibilidade do sistema")
		if dado == "phishing":
			if "vazamento de dados" not in analise:
				analise.append("vazamento de dados")
			if "roubo de credenciais" not in analise:
				analise.append("roubo de credenciais")
			if "perda de desempenho" not in analise:
				analise.append("perda de desempenho")
		if dado == "DDoS":
			if "perda de desempenho" not in analise:
				analise.append("perda de desempenho")
			if "indisponibilidade do sistema" not in analise:
				analise.append("indisponibilidade do sistema")


	analise.append("ciberataque")
	print(analise)
	wait = input("Parada no analisador. Continuar? ")
	infoT, infoNT = moduloDados.gerenciadorDados(3,analise,None)
	#infoNT = verifica_utilidade(infoNT,analise)
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