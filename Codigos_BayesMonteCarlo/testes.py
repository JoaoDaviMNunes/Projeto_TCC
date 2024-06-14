import pandas as pd
import matplotlib.pyplot as plt
import os

# Dados fictícios para o exemplo
saude_malware_media = 10
saude_malware_max = 20
saude_phishing_media = 15
saude_phishing_max = 25
saude_ddos_media = 5
saude_ddos_max = 30

# Criando o DataFrame
plotdata = pd.DataFrame({
    "Malware": [saude_malware_media, saude_malware_max],
    "Phishing": [saude_phishing_media, saude_phishing_max],
    "DDoS": [saude_ddos_media, saude_ddos_max]
}, index=["Médias", "Máximos"])

# Plotando o gráfico de barras
ax = plotdata.plot(kind="bar", figsize=(15, 8), color=['#333333', '#666666', '#999999'])
plt.title("Setor de Saúde: Ataque vs Custo")
plt.xlabel("Tipos de ataques")
plt.ylabel("Custos (em milhões de dólares)")

# Adicionando os valores acima de cada barra
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height}', 
                (p.get_x() + p.get_width() / 2., height + 1),  # +1 to prevent overlapping
                ha='center', va='bottom', fontsize=10, color='black')

# Ajustando as legendas horizontais
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Salvando e mostrando o gráfico
caminho_pasta = "./Imagens"
nome_imagem = 'custosAtaquesSaudeBarras.png'
os.makedirs(caminho_pasta, exist_ok=True)
plt.savefig(os.path.join(caminho_pasta, nome_imagem))
plt.show()
