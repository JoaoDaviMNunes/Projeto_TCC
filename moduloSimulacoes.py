import sys
import os
import csv
import math
import random
import sqlite3
import moduloDados

def gerador_relatorios():
	a = 1
	saida = open('relatorio.pdf', 'w')
	saida.close()

def agrupador_informacoes():
	# .... função
	b = 2
	informacoes = gerenciadorDados()
	gerador_relatorios()

def simulador_riscos(analise):
	# .... função
	gerenciadorDados()
	agrupador_informacoes()

def analisador_negocios(requisicao):
	# .... compreensao da requisicao
	analise = 2
	simulador_riscos(analise)

def main():
	requisicao = sys.argv[1]
	if os.path.exists(requisicao):
		analisador_negocios(requisicao)
	else:
		print('arquivo não existe no diretório')

if __name__ == '__main__':
	main()