import os
import csv
import math
import random
import moduloDados
import sys
import openai
import pandas as pd
import time
import keyboard

# chave do chatGPT
openai.api_key = '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'

# ===========================================================================================================
# FUNÇÃO AUXILIAR
def pause():
	print('Sistema pausado. Para sair, aperte ESPAÇO.')
	while True:
		if keyboard.read_key() == 'space':
			break

# ===========================================================================================================
# POPULADOR DE DADOS
def populador_dados(dados):
	print('POPULADOR DE DADOS')
	moduloDados.gerenciadorDados(2,dados,'')
	pass

# ===========================================================================================================
# CLASSIFICAÇÃO DE RELATÓRIOS
# MODELO DE ANÁLISE DE RELATÓRIOS
def modelo_analise_relatorios(entrada):
	print('MODELO DE ANÁLISE DE RELATÓRIOS')
	print('CLASSIFICAÇÃO DE RELATÓRIOS')
	pesos = [10,5,8,6,5,10]
	for dados in entrada:
		totalSomatorio = (dados[8] + dados[9] + dados[10] + dados[11] + dados[12] + dados [13])/2
		totalPeso = (dados[8]*pesos[0] + dados[9]*pesos[1] + dados[10]*pesos[2] + dados[11]*pesos[3] + dados[12]*pesos[4] + dados[13]*pesos[5])/(pesos[0]+pesos[1]+pesos[2]+pesos[3]+pesos[4]+pesos[5])
		if totalPeso >= 5:
			avaliacao = 'MR'
		elif totalPeso >= 3:
			avaliacao = 'R'
		else:
			avaliacao = 'PR'
		dados.insert(2, avaliacao)

	populador_dados(entrada)
	pass


# ===========================================================================================================
# SELEÇÃO DE MÉTRICAS
def get_completion(prompt, model="gpt-3.5-turbo"):
	messages = [{'role': 'user', 'content': prompt}]
	response = openai.ChatCompletion.create(model=model,messages=messages,temperature=0)
	return response.choices[0].message["content"]


def selecao_metricas(entrada):
	print('SELEÇÃO DE MÉTRICAS')
	for dados in entrada:
		# ... pedir para o chatGPT ranquear a empresa dentro dos nossos critérios (dado[0] = nome da empresa)
		prompt = 'Dada a empresa \''+dados[0]+'''\', responda em um array as classificações da empresa entre 0,1 e 2, conforme as explicações abaixo:
		
		A Reputação da empresa classifica a empresa em relação a sua reputação técnica e maturidade dos processos implementados. A Periodicidade verifica a frequência de publicação de dados que a empresa realiza. Já a  Cobertura verifica o alcance dos relatórios publicados pela empresa, em relação à um país/continente ou com alcance global. O Escopo avalia se o relatório contém informações de um único ou de múltiplos setores/indústrias. A Abrangência dos ataques indica se os relatórios possuem informações sobre mais de um tipo de ataque, sendo relevante para a compreensão da gama de dados contidos no relatório. A Metodologia de Pesquisa tem como foco analisar se a empresa utilizou métodos bem definidos e se os dados obtidos foram satisfatórios.
			
		Reputação  
		0 = Empresa desconhecida   
		1 = Empresa reconhecida nacionalmente   
		2 = Empresa reconhecida mundialmente      
		Periodicidade  
		0 = Compilados de outras fontes   
		1 = Publicação mensal/semestral   
		2 = Publicação anual      
		Cobertura  
		0 = Empresa não menciona   
		1 = Cobertura local/continental   
		2 = Cobertura global      
		Escopo  
		0 = Empresa não menciona   
		1 = Setorial (único)   
		2 = Multisetorial      
		Abrangência dos ataques  
		0 = Empresa não menciona   
		1 = Apenas um tipo de ataque   
		2 = Tipos variados de ataques      
		Metodologia de pesquisa
		0 = Sem metodologia   
		1 = Sem metodologia mas com inferências
		2 = Possuem metodologias e apresentam resultados completos
		
		Apenas responda o array. NÃO envia nenhuma palavra, frase ou texto a mais.'''
		response = get_completion(prompt)
		print(response)
		pause()
		metricasEmpresa = response
		dados.extend(metricasEmpresa)

	modelo_analise_relatorios(entrada)
	pass


# ===========================================================================================================
def main():
	if os.path.exists(sys.argv[1]):
		entrada = sys.argv[1][1:]	#ignora o cabeçalho do arquivo .csv
		selecao_metricas(entrada)
	else:
		print('O arquivo \''+sys.argv[1]+'\' não existe no diretório')

if __name__ == '__main__':
	main()