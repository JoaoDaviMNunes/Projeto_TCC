import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

sectors = ["Financeiro", "Comércio", "Saúde", "Outro"]
attacks = ["Malware", "Phishing", "DDoS"]
divHist = [0, 60000, 120000, 180000, 240000]

iteracoes = 1000

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

'''
Qual setor é a sua empresa (apenas o número):
0 - Financeiro
1 - Comércio
2 - Saúde
3 - Outro
'''
industry = int(input())
'''
Escolha o tipo do ataque (apenas o número):
0 - Malware
1 - Phishing
2 - DDoS
'''
type_attack = int(input())

print("Setor:")
print(sectors[industry])
print("Tipo do ataque:")
print(attacks[type_attack])

infer = pd.read_csv('infer.csv', delimiter=',')
infer.head()

probabilies = monte_carlo_simulation(sectors[industry], attacks[type_attack], infer, iteracoes)
plt.hist(probabilies, divHist) # Histogram plot
plt.show()