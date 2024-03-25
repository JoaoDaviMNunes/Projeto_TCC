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

def agrupador_informacoes():
	informacoes = moduloDados.gerenciadorDados()
	gerador_relatorios()

# ===========================================================================================================
# SIMULADOR DE RISCOS
# Recebe os dados do \textit{Gerenciador de Dados} e utiliza de técnicas matemáticas e probabilísticas para auxiliarem no processo de análise dos riscos e coleta de informações relevantes e referentes à requisição do usuário.
# Os conteúdos a serem simulados levam em conta os dados tangíveis e não tangíveis.

def simulador_riscos(analise):
	# .... função
	moduloDados.gerenciadorDados()
	agrupador_informacoes()

# ===========================================================================================================
# ANALISADOR DE NEGÓCIOS

def analisador_negocios(requisicao):
	# .... compreensao da requisicao
	setor,tpataque,local,ativos = [],[],[],[]

	arquivo = open(requisicao,'r', encoding='utf-8')
	for linha in arquivo:

	arquivo.close()
	analise = [setor,tpataque,local,ativos]
	simulador_riscos(analise)

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