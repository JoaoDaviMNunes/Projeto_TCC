import pandas as pd
import numpy as np
import csv
import sqlite3
import sys

# ===========================================================================================================
# PROCESSADOR DE DADOS
def processador_dados(dados, tab):
	print('PROCESSADOR DE DADOS')
	nometab = ['dadosT', 'dadosNT']
	dadosCorretos = []

	for dado in dados:
		if len(dado) == 15:			# se possui todos os 15 campos
			if not dado[0] and not dado[1] and not dado[7] and not dado[8]:		# se possui os campos essenciais
				if dado[9] != '' and dado[10] != '' and dado[11] != '' and dado[12] != '' and dado[13] != '' and dado[14] != '':		# se possui os campos das métricas
					dadosCorretos.append(dado)

	gerenciadorDados(1, dadosCorretos, nometab[tab])
	print('FECHANDO PROCESSADOR DE DADOS')
	pass

# ===========================================================================================================
# MAPEADOR DE RISCOS

# SALVA NUM ARQUIVO AS LINHAS DE DADOS QUE NÃO ESTÃO FORMATADAS CORRETAMENTE
def salvaErrados_dados(dados):
	print('Alguns dados estão fora do padrão. Olhar o arquivo dadosErradosMAPRIS.csv !')
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
	processador_dados(dadosT, 0)
	processador_dados(dadosNT, 1)
	if len(errados) > 0:
		salvaErrados_dados(errados)
	pass

# ===========================================================================================================
# GERENCIADOR DE DADOS

def cria_tabela(cursor, nometabela):
	try:
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(empresa text NOT NULL, ano int NOT NULL, avaliacao text, dadoA text NOT NULL, dadoB text, probA VARCHAR(5) NOT NULL, probAB VARCHAR(5), refer text NOT NULL, rep int NOT NULL, per int NOT NULL, cob int NOT NULL, esc int NOT NULL, abr int NOT NULL, metod int NOT NULL)")
	except:
		print('Não foi possível criar tabela. Tente novamente!')

def atualizaDado_tabela(cursor, nometabela, nomecampo, valornovo,nomecampopesquisa, valorpesquisa):
	cursor.execute("UPDATE "+nometabela+" SET "+nomecampo+" = "+valornovo+" WHERE "+nomecampopesquisa+" = "+valorpesquisa)

def insereDados_tabela(cursor, row, nometabela):
	empresa = row[0]		# empresa que publicou a informação
	ano = row[1]			# ano referente a pesquisa da publicação
	avaliacao = row[2]		# valor avaliação (feature)
	condicao1 = row[3]		# P(A)
	condicao2 = row[4]		# P(A/B)
	dadoA = row[5] 			# P(A) ou Valor
	dadoB = row[6] 			# P(A|B) ou Métrica
	refer = row[7]			# link do site/da publicação
	rep = row[8]			# valor métrica reputação
	per = row[9]			# valor métrica periodicidade
	cob = row[10]			# valor métrica cobertura
	esc = row[11]			# valor métrica escopo
	abr = row[12]			# valor métrica abrangência dos ataques
	met = row[13]			# valor métrica metodologia
	try:
		cursor.execute("INSERT INTO " + nometabela + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (empresa, ano, avaliacao, condicao1, condicao2, dadoA, dadoB, refer, rep, per, cob, esc, abr, met))
		print("Dados inseridos com sucesso. ")
	except sqlite3.IntegrityError:
		print("Erro: A linha já existe na tabela")

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

	# ... DESENVOLVER ...
 
	print(str(len(tabelas))+' dados encontrads')

	return tabelas

def comandolivre_tabela(cursor):
	command = input('Digite o comando: ')
	try:
		cursor.execute(str(command))
		print("Comando executado com sucesso.")
	except sqlite3.OperationalError as e:
		print("Erro ao executar o comando: ", e)

def gerenciadorDados(acao, material, nometabela):
	bancoDados = 'bancoTCC.db'
	conn = sqlite3.connect(bancoDados)
	cursor = conn.cursor()
	# 1 - vem do Módulo de Relatórios ou das inserções dos curadores e/ou consultores
	# 2 - vem do Mapeador de Riscos (inserção dos dados já tratados)
	# 3 - requisição vindo do Módulo de Simulações a partir das chaves da requisição do usuário
	# 7 - numero para teste (comando livre)
	# 0 - encerrar o módulo de dados
	if acao == 1:
		mapeador_riscos(material)
	elif acao == 2:
		insereDados_tabela(cursor,material,nometabela)
	elif acao == 3:
		dadostabela = buscaDados_tabela(cursor, material)		# nesse caso, material são as chaves desejadas para procurar informações relevantes nas tabelas
		return dadostabela
	elif acao == 7:
			opc = input('Digite o comando que deseja (banco de dados): ')
			repeat = True
			while repeat:
				comandolivre_tabela(cursor)
				ans = input('Deseja tentar mais um comando? (S/N): ')
				if ans == 'N':
					repeat = False

	conn.commit()		# enviando alterações para o banco de dados
	conn.close()		# fechando o acesso ao banco de dados
	print('FECHANDO GERENCIADOR DE DADOS')
	pass

# ===========================================================================================================

def main():
	print('Módulo de Dados!')
	entrada = sys.argv[1]
	gerenciadorDados(7, entrada, 'teste')
	pass

if __name__ == '__main__':
	main()