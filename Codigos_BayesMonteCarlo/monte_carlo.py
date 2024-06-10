import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo
empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Empresa E']
malware = [30, 45, 25, 50, 40]
phishing = [20, 35, 30, 45, 35]
ddos = [25, 20, 40, 30, 20]

# Gráfico de Barras Agrupadas
bar_width = 0.25
x = np.arange(len(empresas))
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width, malware, width=bar_width, label='Malware', color='b')
plt.bar(x, phishing, width=bar_width, label='Phishing', color='g')
plt.bar(x + bar_width, ddos, width=bar_width, label='DDoS', color='r')
plt.title('Distribuição de Porcentagens de Incidentes')
plt.xlabel('Empresas')
plt.ylabel('Porcentagem (%)')
plt.xticks(x, empresas)
plt.ylim(0, 100)
plt.legend()
plt.show()

# Gráfico de Boxplot
dados = [malware, phishing, ddos]
labels = ['Malware', 'Phishing', 'DDoS']
plt.figure(figsize=(8, 6))
plt.boxplot(dados, labels=labels)
plt.title('Distribuição de Porcentagens de Incidentes')
plt.xlabel('Tipo de Incidente')
plt.ylabel('Porcentagem (%)')
plt.ylim(0, 100)
plt.show()

# Gráfico de Dispersão
plt.figure(figsize=(10, 6))
plt.scatter(empresas, malware, color='b', label='Malware', marker='o')
plt.scatter(empresas, phishing, color='g', label='Phishing', marker='s')
plt.scatter(empresas, ddos, color='r', label='DDoS', marker='^')
plt.title('Distribuição de Porcentagens de Incidentes')
plt.xlabel('Empresas')
plt.ylabel('Porcentagem (%)')
plt.ylim(0, 100)
plt.legend()
plt.show()

# Gráfico de Linhas
plt.figure(figsize=(10, 6))
plt.plot(empresas, malware, marker='o', linestyle='-', color='b', label='Malware')
plt.plot(empresas, phishing, marker='s', linestyle='--', color='g', label='Phishing')
plt.plot(empresas, ddos, marker='^', linestyle='-.', color='r', label='DDoS')
plt.title('Distribuição de Porcentagens de Incidentes')
plt.xlabel('Empresas')
plt.ylabel('Porcentagem (%)')
plt.ylim(0, 100)
plt.legend()
plt.show()