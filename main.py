import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics
import math
import random
import sqlite3
import moduloDados



def main():
	entrada = input()

	arquivoCSV1 = 'probabilidades.csv'
	arquivoCSV2 = 'dados.csv'
	nometabela1 = 'probabilidades'
	nometabela2 = 'dados'
	bancoDados = 'bancoTCC.db'
	conn = sqlite3.connect(bancoDados)
	cursor = conn.cursor()

	if entrada == 'livre':
		command = input()
		gerenciadorDados.comandolivre_tabela(cursor, command)
	elif entrada == 'inserir':	

		with open(arquivoCSV1, 'r') as file:
			csv_reader = csv.reader(file)
			headers = next(csv_reader)
			gerenciadorDados.cria_tabela(cursor, nometabela1)

			for row in csv_reader:
				gerenciadorDados.insereDados_tabela(cursor, row, nometabela1)

		with open(arquivoCSV2, 'r') as file2:
			csv_reader2 = csv.reader(file2)
			headers2 = next(csv_reader2)
			gerenciadorDados.cria_tabela(cursor, nometabela2)

			for row in csv_reader2:
				gerenciadorDados.insereDados_tabela(cursor, row, nometabela2)

	conn.commit()
	conn.close()

if __name__ == "__main__":
	main()