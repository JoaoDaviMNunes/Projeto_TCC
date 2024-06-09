import os
import csv
import moduloDados
import sys

# ===========================================================================================================
# POPULADOR DE DADOS
def populador_dados(dados):
	#print('ENTRANDO - POPULADOR DE DADOS')
	moduloDados.gerenciadorDados(1,dados,'')
	#print('FECHANDO - POPULADOR DE DADOS')
	pass

# ===========================================================================================================
# CLASSIFICAÇÃO DE RELATÓRIOS
def classificacao_relatorios(entrada):
	#print('ENTRANDO - CLASSIFICAÇÃO DE RELATÓRIOS')
	pesos = [10,5,8,6,5,10]
	for dados in entrada:
		totalPeso = (int(dados[7])*pesos[0] + int(dados[8])*pesos[1] + int(dados[9])*pesos[2] + int(dados[10])*pesos[3] + int(dados[11])*pesos[4] + int(dados[12])*pesos[5])/(pesos[0]+pesos[1]+pesos[2]+pesos[3]+pesos[4]+pesos[5])*3
		#print(totalPeso)
		if totalPeso >= 5:
			avaliacao = 'MR'
		elif totalPeso >= 3:
			avaliacao = 'R'
		else:
			avaliacao = 'PR'
		dados.insert(2, avaliacao)

	#print('FECHANDO - CLASSIFICAÇÃO DE RELATÓRIOS')
	populador_dados(entrada)
	pass

# ===========================================================================================================
# SELEÇÃO DE MÉTRICAS
def acharIndice(lista, info):
	for indice in range(len(lista)):
		if lista[indice][0] == info:
			return indice
	return -1

def selecao_metricas(entrada):
	#print('ENTRANDO - SELEÇÃO DE MÉTRICAS')

	with open('empresas.csv', 'r',  encoding='utf-8') as arquivoEmpresas:
		empresas = list(csv.reader(arquivoEmpresas))

	with open(entrada, 'r', encoding='utf-8') as arquivo:
		arq = list(csv.reader(arquivo))[1:]
		for dados in arq:
			ind = acharIndice(empresas, dados[0])
			if ind >= 0:
				dados.extend(empresas[ind][1:])
			else:
				print("ERRO => " + str(dados))

	#print('FECHANDO - SELEÇÃO DE MÉTRICAS')
	classificacao_relatorios(arq)
	pass


# ===========================================================================================================
def main():
	if os.path.exists(sys.argv[1]):
		entrada = str(sys.argv[1])	#ignora o cabeçalho do arquivo .csv
		print(entrada)
		selecao_metricas(entrada)
	else:
		print('O arquivo \''+sys.argv[1]+'\' não existe no diretório')
	pass

if __name__ == '__main__':
	main()