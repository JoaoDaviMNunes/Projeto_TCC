import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios
setores = ['Setor 1', 'Setor 2', 'Setor 3']
subcategorias = ['A', 'B', 'C']

# Valores médios, mínimos e máximos para cada subcategoria dentro de cada setor
valores_medios = [
    [4, 7, 1],  # Valores médios para Setor 1
    [2, 6, 3],  # Valores médios para Setor 2
    [5, 8, 2]   # Valores médios para Setor 3
]

valores_minimos = [
    [3, 6, 0.5],  # Valores mínimos para Setor 1
    [1.5, 5, 2.5],  # Valores mínimos para Setor 2
    [4, 7, 1.5]   # Valores mínimos para Setor 3
]

valores_maximos = [
    [5, 8, 1.5],  # Valores máximos para Setor 1
    [2.5, 7, 3.5],  # Valores máximos para Setor 2
    [6, 9, 2.5]   # Valores máximos para Setor 3
]

# Calculando os erros
erros = [[
    [media - minimo, maximo - media] 
    for media, minimo, maximo in zip(val_medios, val_minimos, val_maximos)] 
    for val_medios, val_minimos, val_maximos in zip(valores_medios, valores_minimos, valores_maximos)
]

# Configurando a posição das barras
x = np.arange(len(subcategorias))  # a posição de cada subcategoria

# Largura das barras
width = 0.25  # largura das barras

# Criando a figura e os eixos
fig, ax = plt.subplots()

# Plotando as barras para cada setor
for i, (val, err) in enumerate(zip(valores_medios, erros)):
    err_low = [e[0] for e in err]
    err_high = [e[1] for e in err]
    ax.bar(x + i*width, val, yerr=[err_low, err_high], width=width, capsize=5, label=setores[i])

# Adicionando os rótulos dos eixos
ax.set_ylabel('Valores')
ax.set_xlabel('Subcategorias')
ax.set_title('Gráfico de Barras com Erros por Setor')
ax.set_xticks(x + width)  # ajustando a posição dos rótulos
ax.set_xticklabels(subcategorias)

# Adicionando a legenda
ax.legend()

# Mostrando o gráfico
plt.show()

# -------------------------------------------------------

# Configurando a posição das barras
x = np.arange(len(subcategorias))  # a posição de cada subcategoria

# Largura das barras
width = 0.35  # largura das barras

# Criando figuras e eixos para cada setor
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

for i, (ax, setor, val, err) in enumerate(zip(axs, setores, valores_medios, erros)):
    err_low = [e[0] for e in err]
    err_high = [e[1] for e in err]
    ax.bar(x, val, yerr=[err_low, err_high], width=width, capsize=5, color='skyblue', edgecolor='black')
    ax.set_title(setor)
    ax.set_xticks(x)
    ax.set_xticklabels(subcategorias)
    ax.set_xlabel('Subcategorias')
    if i == 0:
        ax.set_ylabel('Valores')

# Adicionando um título geral ao conjunto de gráficos
plt.suptitle('Gráficos de Barras com Erros por Setor')

# Mostrando os gráficos
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
