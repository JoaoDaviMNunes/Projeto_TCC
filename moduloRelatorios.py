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
	for dados in entrada:
		totalSomatorio = 

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