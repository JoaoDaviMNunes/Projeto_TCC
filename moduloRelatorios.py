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
	moduloDados(dados)

# ===========================================================================================================
# CLASSIFICAÇÃO DE RELATÓRIOS
def classificacao_relatorios(dados):
	print('CLASSIFICAÇÃO DE RELATÓRIOS')
	populador_dados(dados)

# ===========================================================================================================
# MODELO DE ANÁLISE DE RELATÓRIOS
def modelo_analise_relatorios(dados):
	print('MODELO DE ANÁLISE DE RELATÓRIOS')
	classificacao_relatorios(dados)


# ===========================================================================================================
# SELEÇÃO DE MÉTRICAS
def selecao_metricas():
	print('SELEÇÃO DE MÉTRICAS')
	modelo_analise_relatorios(dados)


# ===========================================================================================================
def main():
	teste = 0

if __name__ == '__main__':
	main()