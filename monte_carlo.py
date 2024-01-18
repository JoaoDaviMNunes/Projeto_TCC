import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# definições
sectors = ["Financeiro", "Comércio", "Saúde", "Outro"]
attacks = ["Malware", "Phishing", "DDoS"]
divHist = [0, 60000, 120000, 180000, 240000]
iteracoes = 10000

# funções auxiliares

def attack_occurs(attack_probability): # Definido no .csv
	return np.random.rand() < attack_probability

'''
def attack_loss_amount(lower, upper): # How the values of this function are defined? Normal Distribution.
	mean = (np.log(lower) + np.log(upper))/2.0 
	std_dv = (np.log(upper) - np.log(lower))/3.29
	return np.random.lognormal(mean, std_dv)

def simulate_risk_portfolio(cyber_risks): # Can we define for different assets and scenarios? Yes. We can use as input to calculate the attack_probability.
  total_loss_amount = 0
  for risk in cyber_risks.itertuples():
    if attack_occurs(risk.Probability):
      total_loss_amount += attack_loss_amount(risk.Lower, risk.Upper)
  return total_loss_amount

'''

def simulate_prob(infer):
    return

def monte_carlo_simulation(sectors, attacks, infer, iteracoes):
    probs = []

    # IMPLEMENTAR
    for i in range(iteracoes):
      chance = simulate_prob(infer)
      probs.append(chance)

    return probs

# função main

infer = pd.read_csv('dbprob_20240116.csv', delimiter=',')
infer.head()

probabilies = monte_carlo_simulation(sectors[industry], attacks[type_attack], infer, iteracoes)

# plot (grafico)
plt.hist(probabilies, divHist) # Histogram plot
plt.show()
