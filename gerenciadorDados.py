import os
import pandas as pd
import numpy as np
import csv
import math
import random
import sqlite3

def cria_tabela(cursor, nometabela):
	if nometabela == 'probabilidades':
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(condicao1 text NOT NULL, condicao2 text, probabilidadeA VARCHAR(5) NOT NULL, probabilidadeAB VARCHAR(5), ano integer NOT NULL, empresa text NOT NULL, fonte text NOT NULL)")
	elif nometabela == 'dados':
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(condicao1 text NOT NULL, condicao2 text, valor VARCHAR(10) NOT NULL, metrica text NOT NULL, ano integer NOT NULL, empresa text NOT NULL, fonte text NOT NULL)")

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