import sys
import os
import csv
import math
import random
import sqlite3
import moduloDados
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.styles import getSampleStyleSheet
#from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

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

def gerador_relatorios(info):
	nome_arquivo = "relatoriofinal.pdf"
	'''
	# Cria o documento PDF
	pdf = SimpleDocTemplate(nome_arquivo, pagesize=letter)

	# Estilos para o documento
	estilos = getSampleStyleSheet()
	estilo_titulo = estilos['Title']
	estilo_subtitulo = estilos['Heading2']
	estilo_normal = estilos['BodyText']

	# Conteúdo do PDF
	conteudo = []

	# Adiciona um título
	titulo = Paragraph("Título do Documento", estilo_titulo)
	conteudo.append(titulo)

	# Adiciona um espaço
	conteudo.append(Spacer(1, 12))

	# Adiciona um subtítulo
	subtitulo = Paragraph("Subtítulo do Documento", estilo_subtitulo)
	conteudo.append(subtitulo)

	# Adiciona um parágrafo
	paragrafo = Paragraph("Este é um exemplo de parágrafo no documento PDF. "
	                      "Você pode adicionar mais texto aqui conforme necessário.", estilo_normal)
	conteudo.append(paragrafo)

	# Adiciona um espaço
	conteudo.append(Spacer(1, 12))

	# Adiciona uma imagem (certifique-se de ter uma imagem chamada 'imagem.jpg' no mesmo diretório)
	try:
		imagem = Image('imagem.jpg')
		imagem.drawHeight = 2 * 72
		imagem.drawWidth = 2 * 72
		conteudo.append(imagem)
	except IOError:
		conteudo.append(Paragraph("Imagem não encontrada.", estilo_normal))

	# Constrói o PDF
	pdf.build(conteudo)'''
	print("--------------------------- FIM ---------------------------")

# ===========================================================================================================
# AGRUPADOR DE INFORMAÇÕES
# solicitar ao Gerenciador de Dados as informações relevantes à requisição e informar com precisão quais informações dessas são redirecionadas

def agrupador_informacoes(info):
	gerador_relatorios(info)

# ===========================================================================================================
# SIMULADOR DE RISCOS
def calculo_custo_impacto(impactos, infoT):
	custo_vaz_min, custo_crip_min, custo_des_min, custo_sis_min, custo_cred_min = 0,0,0,0,0
	custo_vaz_max, custo_crip_max, custo_des_max, custo_sis_max, custo_cred_max = 0,0,0,0,0
	custo_vazFinal, custo_cripFinal, custo_desFinal, custo_sisFinal, custo_credFinal = 0,0,0,0,0
	custo_malware_min, custo_phishing_min, custo_ddos_min, custo_cib_min = 0,0,0,0
	custo_malware_max, custo_phishing_max, custo_ddos_max, custo_cib_max = 0,0,0,0
	custo_malwareFinal, custo_phishingFinal, custo_ddosFinal, custo_cibFinal = 0,0,0,0

	for info in infoT:
		#print(info)
		valor = int(info[5])
		if "dólar por ataque" == info[6]:
			if "vazamento de dados" in info[3] or ("vazamento de dados" in info[4] and "custo" in info[3]):
				if custo_vaz_max == 0 and custo_vaz_min == 0:
					custo_vaz_min = valor
					custo_vaz_max = valor
				if valor > custo_vaz_max:
					custo_vaz_max = valor
				if valor < custo_vaz_min:
					custo_vaz_min = valor
			if "dados criptografados" in info[3] or ("dados criptografados" in info[4] and "custo" in info[3]):
				if custo_crip_max == 0 and custo_crip_min == 0:
					custo_crip_min = valor
					custo_crip_max = valor
				if valor > custo_crip_max:
					custo_crip_max = valor
				if valor < custo_crip_min:
					custo_crip_min = valor
			if "perda de desempenho" in info[3] or ("perda de desempenho" in info[4] and "custo" in info[3]):
				if custo_des_max == 0 and custo_des_min == 0:
					custo_des_min = valor
					custo_des_max = valor
				if valor > custo_des_max:
					custo_des_max = valor
				if valor < custo_des_min:
					custo_des_min = valor
			if "indisponibilidade do sistema" in info[3] or ("indisponibilidade do sistema" in info[4] and "custo" in info[3]):
				if custo_sis_max == 0 and custo_sis_min == 0:
					custo_sis_min = valor
					custo_sis_max = valor
				if valor > custo_sis_max:
					custo_sis_max = valor
				if valor < custo_sis_min:
					custo_sis_min = valor
			if "roubo de credenciais" in info[3] or ("roubo de credenciais" in info[4] and "custo" in info[3]):
				if custo_cred_max == 0 and custo_cred_min == 0:
					custo_cred_min = valor
					custo_cred_max = valor
				if valor > custo_cred_max:
					custo_cred_max = valor
				if valor < custo_cred_min:
					custo_cred_min = valor
			if "malware" in info[3] or "malware" in info[4]:
				if custo_malware_min == 0 and custo_malware_max == 0:
					custo_malware_min = valor
					custo_malware_max = valor
				if valor > custo_malware_max:
					custo_malware_max = valor
				if valor < custo_malware_min:
					custo_malware_min = valor
			if "phishing" in info[3] or "phishing" in info[4]:
				if custo_phishing_min == 0 and custo_phishing_max == 0:
					custo_phishing_min = valor
					custo_phishing_max = valor
				if valor > custo_phishing_max:
					custo_phishing_max = valor
				if valor < custo_phishing_min:
					custo_phishing_min = valor
			if "DDoS" in info[3] or "DDoS" in info[4]:
				if custo_ddos_min == 0 and custo_ddos_max == 0:
					custo_ddos_min = valor
					custo_ddos_max = valor
				if valor > custo_ddos_max:
					custo_ddos_max = valor
				if valor < custo_ddos_min:
					custo_ddos_min = valor
			if "ciberataque" in info[3] or "ciberataque" in info[4]:
				if custo_cib_min == 0 and custo_cib_max == 0:
					custo_cib_min = valor
					custo_cib_max = valor
				if valor > custo_cib_max:
					custo_cib_max = valor
				if valor < custo_cib_min:
					custo_cib_min = valor
	
	custo_vazFinal = round(random.uniform(custo_vaz_min, custo_vaz_max),2)
	custo_cripFinal = round(random.uniform(custo_crip_min, custo_crip_max),2)
	custo_desFinal = round(random.uniform(custo_des_min, custo_des_max),2)
	custo_sisFinal = round(random.uniform(custo_sis_min, custo_sis_max),2)
	custo_credFinal = round(random.uniform(custo_cred_min, custo_cred_max),2)
	custo_malwareFinal = round(random.uniform(custo_malware_min, custo_malware_max),2)
	custo_phishingFinal = round(random.uniform(custo_phishing_min, custo_phishing_max),2)
	custo_ddosFinal = round(random.uniform(custo_ddos_min, custo_ddos_max),2)

	custos_impactos = [custo_vazFinal, custo_cripFinal, custo_desFinal, custo_sisFinal, custo_credFinal, custo_malwareFinal, custo_phishingFinal, custo_ddosFinal]
	custos_impactos_sem_zeros = [elemento for elemento in custos_impactos if elemento != 0]

	custoFinal_min = min(custos_impactos_sem_zeros)
	custoFinal_max = max(custos_impactos_sem_zeros)
	custoFinal = round(random.uniform(custoFinal_min, custoFinal_max),2)
	
	return custoFinal

	


def add_impactos(impactos, tps_impactos):
	for i in range(len(impactos)):
		if impactos[i] < tps_impactos[i]:
			impactos[i] = 1
	return impactos

def montecarlo_simulacao_ataque(rodadas, prob_ataque, prob_impactos):
	'''
	prob_ataque = lista de todas probabilidades de ocorrer o ataque
	prob_impactos = lista com a média das probabilidades de ocorrer os impactos
	prob_impactos[0] = vazamento de dados (malware e phishing)
	prob_impactos[1] = dados criptografados (malware)
	prob_impactos[2] = perda de desempenho (malware, phishing e DDoS)
	prob_impactos[3] = indisponibilidade do sistema (malware e DDoS)
	prob_impactos[4] = roubo de credenciais (phishing)
	'''

	contadorAtaque = 0
	contadorImpacto = [0,0,0,0,0]

	#print("PROB ATAQUE - " + str(prob_ataque) + ' - ' + str(len(prob_ataque)))
	#print("PROB IMPACTOS - " + str(prob_impactos) + ' - ' + str(len(prob_impactos)))

	for _ in range(rodadas):
		pos = random.randint(0, len(prob_ataque)-1)
		if random.random() <= (prob_ataque[pos]/100):
			contadorAtaque += 1
			if random.random() <= prob_impactos[0]: # vazamento de dados (malware e phishing)
				#print("VAZAMENTO DE DADOS")
				contadorImpacto[0] += 1
			if random.random() <= prob_impactos[1]: # dados criptografados (malware)
				#print("DADOS CRIPTOGRAFADOS")
				contadorImpacto[1] += 1
			if random.random() <= prob_impactos[2]: # perda de desempenho (malware, phishing e DDoS)
				#print("PERDA DE DESEMPENHO")
				contadorImpacto[2] += 1
			if random.random() <= prob_impactos[3]: # indisponibilidade do sistema (malware e DDoS)
				#print("INDISPONIBILIDADE DO SISTEMA")
				contadorImpacto[3] += 1
			if random.random() <= prob_impactos[4]: # roubo de credenciais (phishing)
				#print("ROUBO DE CREDENCIAIS")
				contadorImpacto[4] += 1
	
	probFinalAtaque = round(contadorAtaque/rodadas*100,2)
	probFinalVaz = round(contadorImpacto[0]/contadorAtaque*100,2)
	probFinalCrip = round(contadorImpacto[1]/contadorAtaque*100,2)
	probFinalDes = round(contadorImpacto[2]/contadorAtaque*100,2)
	probFinalInd = round(contadorImpacto[3]/contadorAtaque*100,2)
	probFinalCred = round(contadorImpacto[4]/contadorAtaque*100,2)
	return probFinalAtaque, [probFinalVaz, probFinalVaz, probFinalCrip, probFinalDes, probFinalInd, probFinalCred]

def simulador_riscos(infoT, infoNT, tudo):

	final = []
	riscoM, riscoP, riscoD = [],[],[]										# contator total das porcentagens de cada ataque
	impVaz, impCrip, impDes, impInd, impCred = 0,0,0,0,0 					# contador total das porcentagens de sucesso de cada impacto
	cm, cp, cd = 0,0,0														# contador de itens de cada ataque
	contVaz, contCrip, contDes, contInd, contCred = 0,0,0,0,0 				# contador de itens de cada impacto
	probM_impactos, probP_impactos, probD_impactos = 0,0,0 					# probabilidade de ocorrer cada impacto, dependendo do tipo de ataque
	prob_ataque_malware, prob_ataque_phishing, prob_ataque_ddos = 0,0,0 	# probabilidade de ocorrer cada tipo de ataque
	ciber = 0

	# VERIFICAR OS RISCOS E OS IMPACTOS DA EMPRESA SOFRER O RISCO DO ATAQUE
	for info in infoNT:		
		risco = 0
		if info[5] != "-":
			risco = float(info[5])
		else:
			risco = float(info[6])

		if ("malware" in info[3] or "ransomware" in info[3] or "ciberataque" in info[3]) and tudo[3] == '1':
			riscoM.append(risco)
			cm += 1	
		if ("phishing" in info[3] or "ciberataque" in info[3]) and tudo[4] == '1':
			riscoP.append(risco)
			cp += 1
		if ("DDoS" in info[3] or "ciberataque" in info[3]) and tudo[5] == '1':
			riscoD.append(risco)
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

	prob_impactos = [round(contVaz/impVaz if impVaz else 0,2),
				round(contCrip/impCrip if impCrip else 0,2),
				round(contDes/impDes if impDes else 0,2),
				round(contInd/impInd if impInd else 0,2),
				round(contCred/impCred if impCred else 0,2)]

	print("Nº_DADOS M - " + str(len(riscoM)))
	print("Nº_DADOS P - " + str(len(riscoP)))
	print("Nº_DADOS D - " + str(len(riscoD)))

	# verifica via simulação quais são os riscos e impactos de cada tipo de ataque
	if cm > 0:
		prob_ataque_malware, probM_impactos = montecarlo_simulacao_ataque(rodadas, riscoM, prob_impactos)
	if cp > 0:
		prob_ataque_phishing, probP_impactos = montecarlo_simulacao_ataque(rodadas, riscoP, prob_impactos)
	if cd > 0:
		prob_ataque_ddos, probD_impactos = montecarlo_simulacao_ataque(rodadas, riscoD, prob_impactos)
	final.append([prob_ataque_malware, probM_impactos])
	final.append([prob_ataque_phishing, probP_impactos])
	final.append([prob_ataque_ddos, probD_impactos])

	# PRINTANDO PARA SABER O STATUS ----> tais informações irão para o relatório e não serão printadas na tela
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

	# VERIFICAR O RISCO FINANCEIRO (infoT)
	impactos = [0,0,0,0,0]
	if int(tudo[3]) == 1:
		impactos = add_impactos(impactos, [1,1,1,1,0])
	if int(tudo[4]) == 1:
		impactos = add_impactos(impactos, [1,0,1,0,1])
	if int(tudo[5]) == 1:
		impactos = add_impactos(impactos, [0,0,1,1,0])

	custoFinal = calculo_custo_impacto(impactos, infoT)
	print("Custo final: " + str(custoFinal))
	final.append(custoFinal)

	agrupador_informacoes(final)

# ===========================================================================================================
# ANALISADOR DE NEGÓCIOS

# verifica se todas as informações dos campos infoA e infoB são referentes ao que estamos pesquisando
def verifica_utilidade(infoNT, analise):
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
	'''for info in infosCertas:
		print(info)'''
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
				for pais in paisesAPAC:
					analise.append(pais)
			if arquivo[linha][1] == "1":
				analise.append("LATAM")
				for pais in paisesLATAM:
					analise.append(pais)
			if arquivo[linha][2] == "1":
				analise.append("EMEA")
				for pais in paisesEMEA:
					analise.append(pais)
			if arquivo[linha][3] == "1":
				analise.append("NA")
				for pais in paisesNA:
					analise.append(pais)

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
	infoT, infoNT = moduloDados.gerenciadorDados(3,analise,None)
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

if __name__ == "__main__":
	main()