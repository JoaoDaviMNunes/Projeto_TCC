import os
import random
from random import seed
from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics
import math
from sklearn.metrics import confusion_matrix
import seaborn as sns
import random
import sqlite3

def cria_tabela():
	bancoDados = sqlite3.connect('bancoTCC.db')
	cursor = bancoDados.cursor()
	cursor.execute("CREATE TABLE probabilidades (condicao1 text, condicao2 text, probabilidade VARCHAR(5) NOT NULL, ano integer NOT NULL, fonte text NOT NULL)")
	bancoDados.commit()

	