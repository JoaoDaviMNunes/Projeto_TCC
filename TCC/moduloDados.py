import csv
import sqlite3
import sys

# ===========================================================================================================
# VALIDADOR DE DADOS
def validador_dados(dados, tab):
	#print('ENTRANDO - PROCESSADOR DE DADOS')
	nometab = ['dadosTang', 'dadosNTang']
	dadosCorretos = []

	for dado in dados:
		if len(dado) == 14:			# se possui todos os 14 campos
			if dado[0] != None and dado[1] != None and dado[3] != None and (dado[5] != None or dado[7] != None):		# se possui os campos essenciais (empresa, ano, dadoA e P(A) ou P(B))
				if dado[8] != None and dado[9] != None and dado[10] != None and dado[11] != None and dado[12] != None and dado[13] != None:		# se possui os campos das métricas
					dadosCorretos.append(dado)

	#print("Dados corretos:", dadosCorretos)
	gerenciadorDados(2, dadosCorretos, nometab[tab])
	#print('FECHANDO - PROCESSADOR DE DADOS')
	pass

# ===========================================================================================================
# MAPEADOR DE RISCOS

# SALVA NUM ARQUIVO AS LINHAS DE DADOS QUE NÃO ESTÃO FORMATADAS CORRETAMENTE
def salvaErrados_dados(dados):
	print('Alguns dados estão fora do padrão. Olhar o arquivo dadosErradosMAPRIS.csv !')
	with open('dadosErradosMAPRIS.csv', 'w', encoding='utf-8') as csvfile:
		csvfinal = csv.writer(csvfile)
		csvfinal.writerows(dados)
		print('Arquivo dos dados errados foi criado!')
	pass

# VERIFICA SE O DADO É TANGÍVEL OU NÃO
def mapeador_riscos(dados):
	#print('ENTRANDO - MAPEADOR DE RISCOS')
	dadosT = []			# dados tangíveis
	dadosNT = []		# dados não tangíveis
	errados = []

	for dado in dados:
		info = dado[6]			# dadoAB/métrica (T/NT)
		if info.replace('.','',1).isdigit() or info == '-':
			dadosNT.append(dado)
		elif isinstance(info, str):
			dadosT.append(dado)
		else:
			errados.append(dado)

	if len(dadosT) > 0:
		#print("Tam dadosTang = "+str(len(dadosT)))
		validador_dados(dadosT, 0)
	if len(dadosNT) > 0:
		#print("Tam dadosNTang = "+str(len(dadosNT)))
		validador_dados(dadosNT, 1)
	if len(errados) > 0:
		salvaErrados_dados(errados)
	#print('FECHANDO - MAPEADOR DE RISCOS')
	pass

# ===========================================================================================================
# GERENCIADOR DE DADOS

def cria_tabela(cursor, nometabela):
	try:
		cursor.execute("CREATE TABLE IF NOT EXISTS "+nometabela+"(empresa text NOT NULL, ano text NOT NULL, avaliacao text, dadoA text NOT NULL, dadoB text, probA text NOT NULL, probAB text, refer text NOT NULL, rep text NOT NULL, per text NOT NULL, cob text NOT NULL, esc text NOT NULL, abr text NOT NULL, metod text NOT NULL)")
	except:
		print('Não foi possível criar tabela. Tente novamente!')

def atualizaDado_tabela(cursor, nometabela, nomecampo, valornovo, nomecampopesquisa, valorpesquisa):
	cursor.execute("UPDATE "+nometabela+" SET "+nomecampo+" = "+valornovo+" WHERE "+nomecampopesquisa+" = "+valorpesquisa)
	pass

def insereDados_tabela(cursor, row, nometabela):
	#print(nometabela)
	for linha in row:
		empresa = linha[0]		# empresa que publicou a informação
		ano = linha[1]			# ano referente a pesquisa da publicação
		avaliacao = linha[2]		# valor avaliação (feature)
		dadoA = linha[3]		# P(A)
		dadoB = linha[4]		# P(A/B)
		probA = linha[5] 			# P(A) ou Valor
		probAB = linha[6] 			# P(A|B) ou Métrica
		refer = linha[7]			# link do site/da publicação
		rep = linha[8]			# valor métrica reputação
		per = linha[9]			# valor métrica periodicidade
		cob = linha[10]			# valor métrica cobertura
		esc = linha[11]			# valor métrica escopo
		abr = linha[12]			# valor métrica abrangência dos ataques
		metod = linha[13]			# valor métrica metodologia
		params = (empresa,ano,avaliacao,dadoA,dadoB,probA,probAB,refer,rep,per,cob,esc,abr,metod)
		#print(params)

		if nometabela == "dadosNTang":
			try:
				cursor.execute("""
					INSERT INTO dadosNTang 
					SELECT ?,?,?,?,?,?,?,?,?,?,?,?,?,? 
					WHERE NOT EXISTS (
						SELECT 1 FROM dadosNTang 
						WHERE empresa=? AND ano=? AND avaliacao=? AND dadoA=? AND dadoB=? 
						AND probA=? AND probAB=? AND refer=? AND rep=? AND per=? AND cob=? 
						AND esc=? AND abr=? AND metod=?
					)
				""", (*params, *params))
				print("Dados inseridos com sucesso.")
			except sqlite3.IntegrityError:
				print("Erro: A linha já existe na tabela")
		else:
			try:
				cursor.execute("""
					INSERT INTO dadosTang 
						SELECT ?,?,?,?,?,?,?,?,?,?,?,?,?,? 
						WHERE NOT EXISTS (
						SELECT 1 FROM dadosTang 
						WHERE empresa=? AND ano=? AND avaliacao=? AND dadoA=? AND dadoB=? 
						AND probA=? AND probAB=? AND refer=? AND rep=? AND per=? AND cob=? 
						AND esc=? AND abr=? AND metod=?
					)
				""", (*params, *params))
				print("Dados inseridos com sucesso.")
			except sqlite3.IntegrityError:
				print("Erro: A linha já existe na tabela")
	pass

def deletaItem_tabela(cursor, nometabela, condicao):
	try:
		cursor.execute("DELETE from " + nometabela + " WHERE " + condicao)
		print("Dados removidos")
	except sqlite3.Error as erro:
		print ("Erro ao excluir: ", erro)

def mostra_tabela(cursor, nometabela):
	cursor.execute("SELECT * from " + nometabela)
	print(cursor.fetchall())

def buscaDados_tabela(cursor, chaves):
	infoT, infoNT = [],[]

	for chave in chaves:
		cursor.execute("SELECT * FROM dadosTang WHERE dadoA LIKE ?", ('%' + chave + '%',))
		resposta = cursor.fetchall()
		if resposta != None:
			infoT.extend(resposta)
		cursor.execute("SELECT * FROM dadosTang WHERE dadoB LIKE ?", ('%' + chave + '%',))
		resposta = cursor.fetchall()
		if resposta != None:
			infoT.extend(resposta)

		cursor.execute("SELECT * FROM dadosNTang WHERE dadoA LIKE ?", ('%' + chave + '%',))
		resposta = cursor.fetchall()
		if resposta != None:
			infoNT.extend(resposta)
		cursor.execute("SELECT * FROM dadosNTang WHERE dadoB LIKE ?", ('%' + chave + '%',))
		resposta = cursor.fetchall()
		if resposta != None:
			infoNT.extend(resposta)

		#wait = input("Pausa:")
	
	#print(str(len(infoT))+' dadosTang e '+ str(len(infoNT))+' dadosNTang')

	# removendo os itens duplicados
	infoT = list(dict.fromkeys(infoT))
	infoNT = list(dict.fromkeys(infoNT))
	return infoT, infoNT

def comandolivre_tabela(cursor, command):
	try:
		cursor.execute(str(command))
		print("Comando executado com sucesso.")
	except sqlite3.OperationalError as e:
		print("Erro ao executar o comando! => ", e)

def gerenciadorDados(acao, material, nometabela):
	#print('ENTRANDO - GERENCIADOR DE DADOS')
	bancoDados = 'bancoTCC.db'
	conn = sqlite3.connect(bancoDados)
	cursor = conn.cursor()

	cria_tabela(cursor, "dadosNTang")
	cria_tabela(cursor, "dadosTang")
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
		infoT, infoNT = buscaDados_tabela(cursor, material)		# nesse caso, material são as chaves desejadas para procurar informações relevantes nas tabelas
		return infoT, infoNT
	elif acao == 7:
			repeat = True
			while repeat:
				opc = input('Digite o comando que deseja (banco de dados): ')
				comandolivre_tabela(cursor,opc)
				ans = input('Deseja tentar mais um comando? (S/N): ')
				if ans == 'N' or ans == 'n':
					repeat = False

	conn.commit()		# enviando alterações para o banco de dados
	conn.close()		# fechando o acesso ao banco de dados
	#print('FECHANDO - GERENCIADOR DE DADOS')
	pass

# ===========================================================================================================

def main():
	if len(sys.argv) >= 2:
		entrada = sys.argv[1]
		gerenciadorDados(1, entrada, 'teste')
	else:
		gerenciadorDados(7, [], 'teste')
	pass

if __name__ == '__main__':
	main()