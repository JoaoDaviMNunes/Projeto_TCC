import sys
import os
import csv
import math
import random
import sqlite3
import moduloDados

# ===========================================================================================================
# GERADOR DE RELATÓRIOS
# Recebe, condensa, organiza e formata as informações, de forma a gerar um relatório completo para o usuário.
# Este relatório dispõe de uma análise da empresa (informada na requisição do usuário), como sua estimativa de tamanho, porte econômico e ativos importantes. 
# Este documento igualmente contém o risco da empresa de sofrer um ciberataque de Malware, Phishing e DDoS, com base nas simulações realizadas previamente.

def gerador_relatorios():
	saida = open('relatorio.pdf', 'w')

	# ...
	
	saida.close()

# ===========================================================================================================
# AGRUPADOR DE INFORMAÇÕES
# solicitar ao Gerenciador de Dados as informações relevantes à requisição e informar com precisão quais informações dessas são redirecionadas

def agrupador_informacoes(info):
	gerador_relatorios()

# ===========================================================================================================
# SIMULADOR DE RISCOS
# Recebe os dados do \textit{Gerenciador de Dados} e utiliza de técnicas matemáticas e probabilísticas para auxiliarem no processo de análise dos riscos e coleta de informações relevantes e referentes à requisição do usuário.
# Os conteúdos a serem simulados levam em conta os dados tangíveis e não tangíveis.

def simulador_riscos(infoT, infoNT):
	# .... função
	wait = input("Parada no simulador. Continuar? ")
	agrupador_informacoes()

# ===========================================================================================================
# ANALISADOR DE NEGÓCIOS

def analisador_negocios(requisicao):
	print("ENTRANDO - ANALISADOR DE NEGÓCIOS")
	analise = []
	arquivo = list(open(requisicao,'r', encoding='utf-8'))

	for linha in range(len(arquivo)):
		if linha == 0:
			print("Setor = " + str(arquivo[linha]))
			if arquivo[linha][0] == '1':
				analise.append("setor financeiro")
			if arquivo[linha][1] == '1':
				analise.append("setor de saúde")
			if arquivo[linha][2] == '1':
				analise.append("setor de comércio")
		elif linha == 1:
			print("Tipo de ataque = " + str(arquivo[linha]))
			if arquivo[linha][0] == '1':
				analise.append("malware")
				analise.append("ransomware")
			if arquivo[linha][1] == '1':
				analise.append("phishing")
			if arquivo[linha][2] == '1':
				analise.append("DDoS")
		elif linha == 2:
			print("Local = " + str(arquivo[linha]))
			if arquivo[linha][0] == '1':
				analise.append("América do Sul")
			if arquivo[linha][1] == '1':
				analise.append("América do Norte")
			if arquivo[linha][2] == '1':
				analise.append("Europa")
			if arquivo[linha][3] == '1':
				analise.append("Ásia")
			if arquivo[linha][4] == '1':
				analise.append("Oceania")
			if arquivo[linha][5] == '1':
				analise.append("África")

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
		print('O arquivo '+requisicao+' não existe no diretório')
	print('Arquivo de saída gerado!')

if __name__ == '__main__':
	main()