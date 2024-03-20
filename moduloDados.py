import os
import pandas as pd
import numpy as np
import csv
import math
import random
import sqlite3
import sys

# ===========================================================================================================
# MAPEADOR DE RISCOS
def mapeador_riscos(dados):
	return dados

# ===========================================================================================================
# PROCESSADOR DE DADOS
def processador_dados(dados):
	return mapeador_riscos(dados)

# ===========================================================================================================
# GERENCIADOR DE DADOS

def cria_tabela(cursor, nometabela):
	if nometabela == 'probabilidades':
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(condicao1 text NOT NULL, condicao2 text, probabilidadeA VARCHAR(5) NOT NULL, probabilidadeAB VARCHAR(5), ano integer NOT NULL, empresa text NOT NULL, fonte text NOT NULL)")
	elif nometabela == 'dados':
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(condicao1 text NOT NULL, condicao2 text, valor VARCHAR(10) NOT NULL, metrica text NOT NULL, ano integer NOT NULL, empresa text NOT NULL, fonte text NOT NULL)")
	else:
		print('nenhuma das tabelas base. tente novamente!')

def atualizaDado_tabela(cursor, nometabela, valornovo,nomecampopesquisa, valorpesquisa):
	cursor.execute("UPDATE "+nometabela+" SET "+nomecampo+" = "+valornovo+" WHERE "+nomecampopesquisa+" = "+valorpesquisa)

def insereDados_tabela(cursor, row, nometabela):
	condicao1 = row[0]
	condicao2 = row[1]
	dadoA = row[2] # P(A) ou Valor
	dadoB = row[3] # P(A|B) ou Métrica
	ano = row[4]
	empresa = row[5]
	fonte = row[6]
	try:
		cursor.execute("INSERT INTO " + nometabela + " VALUES (?, ?, ?, ?, ?, ?, ?)", (condicao1, condicao2, dadoA, dadoB, ano, empresa, fonte))
		print("Dados inseridos com sucesso. ")
	except sqlite3.IntegrityError:
		print("Erro: A linha já existe na tabe")

def deletaItem_tabela(cursor, nometabela, condicao):
	try:
		cursor.execute("DELETE from " + nometabela + " WHERE " + condicao)
		print("Dados removidos")
	except sqlite3.Error as erro:
		print ("Erro ao excluir:", erro)

def mostra_tabela(cursor, nometabela):
	cursor.execute("SELECT * from " + nometabela)
	print(cursor.fetchall())

def comandolivre_tabela(cursor, command):
	try:
		cursor.execute(''+command+'')
		print("Comando executado com sucesso.")
	except sqlite3.OperationalError as e:
		print("Erro ao executar o comando:", e)

def gerenciadorDados(acao, material, nometabela):
	conn = sqlite3.connect(bancoDados)
	cursor = conn.cursor()
	# 1 - vem do Mapeador de Riscos (inserção especial - dados tratados)
	# 2 - vem do Módulo de Relatórios ou dos curadores e consultores (inserção normal)
	# 3 - vem do Módulo de Simulações (requisição)
	# 7 - numero para teste (comando livre)
	# 0 - encerrar o módulo de dados
	while acao:
		if acao == 1:
			insereDados_tabela(cursor,material,nometabela)
			break
		elif acao == 2:
			insereDados_tabela()




		



# ===========================================================================================================

def main():
	print('Módulo de Dados!')
	print('Digite o que deseja')
	opc = input()
	comandolivre_tabela(cursor, opc)

	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()