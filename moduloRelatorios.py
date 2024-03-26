import os
import csv
import math
import random
import moduloDados
import sys

# ===========================================================================================================
# POPULADOR DE DADOS
def populador_dados(dados):
	print('POPULADOR DE DADOS')
	moduloDados.gerenciadorDados(2,dados,'')

# ===========================================================================================================
# CLASSIFICAÇÃO DE RELATÓRIOS
def classificacao_relatorios(dados):
	print('CLASSIFICAÇÃO DE RELATÓRIOS')
	populador_dados(dados)
	pass

# ===========================================================================================================
# MODELO DE ANÁLISE DE RELATÓRIOS
def modelo_analise_relatorios(entrada):
	print('MODELO DE ANÁLISE DE RELATÓRIOS')
	pesos = [10,5,8,6,5,10]
	for dados in entrada:
		totalSomatorio = (dados[8] + dados[9] + dados[10] + dados[11] + dados[12] + dados [13])/2
		totalPeso = (dados[8]*pesos[0] + dados[9]*pesos[1] + dados[10]*pesos[2] + dados[11]*pesos[3] + dados[12]*pesos[4] + dados[13]*pesos[5])/(pesos[0]+pesos[1]+pesos[2]+pesos[3]+pesos[4]+pesos[5])
		

	classificacao_relatorios(entrada)
	pass


# ===========================================================================================================
# SELEÇÃO DE MÉTRICAS
def selecao_metricas(entrada):
	print('SELEÇÃO DE MÉTRICAS')
	for dados in entrada:
		# ... pedir para o chatGPT ranquear a empresa dentro dos nossos critérios (dado[0] = nome da empresa)
		metricasEmpresa = 1 # query chatGPT
		dados.extend(metricasEmpresa)

	modelo_analise_relatorios(entrada)
	pass


# ===========================================================================================================
def main():
	if os.path.exists(sys.argv[1]):
		entrada = sys.argv[1]
		selecao_metricas(entrada)
	else:
		print('O arquivo \''+sys.argv[1]+'\' não existe no diretório')

if __name__ == '__main__':
	main()