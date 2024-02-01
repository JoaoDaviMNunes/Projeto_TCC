import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
	
cyber_risks = pd.read_csv('cyber_risks.csv', delimiter=',')
cyber_risks.head()

def attack_occurs(attack_probability): # Defined in the CSV
	return np.random.rand() < attack_probability

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

def monte_carlo_simulation(cyber_risks, iterations): # What happen here in this function exactly? Use the probability of an event occurs and the mean of the loss amount.
  yearly_losses = []
  for i in range(iterations):
    loss_amount = simulate_risk_portfolio(cyber_risks)
    yearly_losses.append(loss_amount)
  return yearly_losses

yearly_losses = monte_carlo_simulation(cyber_risks, iterations = 100000) # 1000 simulations
#print(yearly_losses)


plt.hist(yearly_losses, bins=[0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 260000]) # Histogram plot
plt.show()

