import sys
import os
import csv
import math
import random
import sqlite3
import moduloDados

# ===========================================================================================================
# GERADOR DE RELATÓRIOS

def gerador_relatorios():
	a = 1
	saida = open('relatorio.pdf', 'w')

	# ... CORAÇÃO DA FUNÇÃO
	
	saida.close()

# ===========================================================================================================
# AGRUPADOR DE INFORMAÇÕES

def agrupador_informacoes():
	# .... função
	b = 2
	informacoes = moduloDados.gerenciadorDados()
	gerador_relatorios()

# ===========================================================================================================
# SIMULADOR DE RISCOS

def simulador_riscos(analise):
	# .... função
	gerenciadorDados()
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