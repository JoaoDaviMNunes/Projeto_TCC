# https://thepythoncodingbook.com/basics-of-data-visualisation-in-python-using-matplotlib/

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed"]
steps_walked = [8934, 14902, 3409]
steps_walked2 = [2156, 20563, 1500]
steps_walked3 = [4590, 5000, 10000]
plt.plot(days, steps_walked, color='grey', linewidth=3, marker='o', markersize=8, linestyle='--', label='Linha 1')
plt.plot(days, steps_walked2, "s-", color='grey', linewidth=3, marker='s', markersize=8, linestyle='-', label='Linha 2')
plt.plot(days, steps_walked3, "^-", color='grey', linewidth=3, marker='^', markersize=8, linestyle='-', label='Linha 3')
for i, txt in enumerate(steps_walked):
    plt.annotate(txt, (days[i], steps_walked[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')
for i, txt in enumerate(steps_walked2):
    plt.annotate(txt, (days[i], steps_walked2[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')
for i, txt in enumerate(steps_walked3):
    plt.annotate(txt, (days[i], steps_walked3[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')
plt.title("Título")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.tight_layout()
plt.show()

# Inicializando os dados
x = [10, 20, 30, 40]
y1 = [20, 25, 35, 55]
y2 = [15, 30, 25, 50]
y3 = [10, 20, 30, 40]

# Plotando as linhas
plt.plot(x, y1, color='green', linewidth=3, marker='o', markersize=8, linestyle='--', label='Linha 1')
plt.plot(x, y2, color='blue', linewidth=3, marker='s', markersize=8, linestyle='-', label='Linha 2')
plt.plot(x, y3, color='red', linewidth=3, marker='^', markersize=8, linestyle=':', label='Linha 3')

# Adicionando título ao gráfico
plt.title("Gráfico de Linhas com Três Linhas")

# Adicionando rótulo no eixo y
plt.ylabel('Eixo Y')

# Adicionando rótulo no eixo x
plt.xlabel('Eixo X')

# Adicionando uma legenda
plt.legend()

# Mostrando o gráfico
plt.show()
