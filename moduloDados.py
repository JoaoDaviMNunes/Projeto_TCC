import pandas as pd
import numpy as np
import csv
import sqlite3

# ===========================================================================================================
# PROCESSADOR DE DADOS
def processador_dados(dados):
	print('PROCESSADOR DE DADOS')

	for dado in dados:
		if len(dado) == 15:			# se possui todos os 15 campos
			if not dado[0] and not dado[1] and not dado[7] and not dado[8]:		# se possui os campos essenciais
				if dado[9] != '' and dado[10] != '' and dado[11] != '' and dado[12] != '' and dado[13] != '' and dado[14] != '':		# se possui os campos das métricas
					if dado[4] == '-':
						gerenciadorDados(1, dado, XXXXX)

	print('FECHANDO PROCESSADOR DE DADOS')
	mapeador_riscos(dados)
	pass

# ===========================================================================================================
# MAPEADOR DE RISCOS

# SALVA NUM ARQUIVO AS LINHAS DE DADOS QUE NÃO ESTÃO FORMATADAS CORRETAMENTE
def salvaErrados_dados(dados):
	print('Alguns dados estão fora do padrão. Olhar o arquivo dadosErrados.csv !')
	with open('dadosErradosMAPRIS.csv', 'w', encoding='utf-8') as csvfile:
		csvfinal = csv.writer(csvfile)
		csvfinal.writerows(dados)
		print('Arquivo criado!')
	pass

# VERIFICA SE O DADO É TANGÍVEL OU NÃO
def mapeador_riscos(dados):
	print('MAPEADOR DE RISCOS')
	dadosT = []			# dados tangíveis
	dadosNT = []		# dados não tangíveis
	errados = []

	for dado in dados:
		info = dado[6]			# dadoAB/métrica (T/NT)
		if isinstance(info, float) or isinstance(info, int):
			dadosNT.append(dado)
		elif isinstance(info, str):
			dadosT.append(dado)
		else:
			errados.append(dado)

	print('FECHANDO MAPEADOR DE RISCOS')
	processador_dados(dadosNT)
	processador_dados(dadosT)
	if len(errados) == 0:
		salvaErrados_dados(errados)
	pass

# ===========================================================================================================
# GERENCIADOR DE DADOS

def cria_tabela(cursor, nometabela):
	if nometabela == 'probabilidades':
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(condicao1 text NOT NULL, condicao2 text, probabilidadeA VARCHAR(5) NOT NULL, probabilidadeAB VARCHAR(5), ano integer NOT NULL, empresa text NOT NULL, fonte text NOT NULL)")
	elif nometabela == 'dados':
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(condicao1 text NOT NULL, condicao2 text, valor VARCHAR(10) NOT NULL, metrica text NOT NULL, ano integer NOT NULL, empresa text NOT NULL, fonte text NOT NULL)")
	else:
		print('nenhuma das tabelas base. tente novamente!')

def atualizaDado_tabela(cursor, nometabela, nomecampo, valornovo,nomecampopesquisa, valorpesquisa):
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
		print ("Erro ao excluir: ", erro)

def mostra_tabela(cursor, nometabela):
	cursor.execute("SELECT * from " + nometabela)
	print(cursor.fetchall())

def defineChaves(material):
	chaves = []

	# ... DESENVOLVER ...
	
	return chaves

def buscaDados_tabela(cursor, chaves):
	tabelas = []
	return tabelas

def comandolivre_tabela(cursor, command):
	try:
		cursor.execute(''+command+'')
		print("Comando executado com sucesso.")
	except sqlite3.OperationalError as e:
		print("Erro ao executar o comando:", e)

def gerenciadorDados(acao, material, nometabela):
	bancoDados = 'bancoTCC.db'
	conn = sqlite3.connect(bancoDados)
	cursor = conn.cursor()
	# 1 - vem do Mapeador de Riscos (inserção especial - dados tratados)
	# 2 - vem do Módulo de Relatórios ou dos curadores e consultores (inserção normal)
	# 3 - vem do Módulo de Simulações (requisição)
	# 7 - numero para teste (comando livre)
	# 0 - encerrar o módulo de dados
	if acao == 1:
		insereDados_tabela(cursor,material,nometabela)
	elif acao == 2:
		insereDados_tabela(cursor, material,nometabela)
	elif acao == 3:
		chaves = defineChaves(material)
		buscaDados_tabela(cursor, chaves)
	elif acao == 7:
			opc = input('Digite o comando que deseja (banco de dados): ')
			comandolivre_tabela(cursor, opc)
	elif acao == 0:
		pass

	conn.commit()		# enviando alterações para o banco de dados
	conn.close()		# fechando o acesso ao banco de dados
	print('FECHANDO GERENCIADOR DE DADOS')
	pass

		



# ===========================================================================================================

def main():
	print('Módulo de Dados!')
	gerenciadorDados()
	pass

if __name__ == '__main__':
	main()