import sys
import os
import ast
import matplotlib.pyplot as plt
import numpy as np

setores = ['Financeiro', 'Comércio', 'Saúde']

def main():
    dado_lst = []
    malware_min,malware_medio,malware_max = 0,0,0
    phishing_min,phishing_medio,phishing_max = 0,0,0
    ddos_min,ddos_medio,ddos_max = 0,0,0

    financeiro_min,financeiro_medio,financeiro_max = 0,0,0
    comercio_min,comercio_medio,comercio_max = 0,0,0
    saude_min,saude_medio,saude_max = 0,0,0

    malware_media, phishing_media, ddos_media = 0,0,0
    numM, numP, numD = 0,0,0

    for i in range(100):    
        nome_arquivo = "./Resultados/rodada" + str(i) + ".txt"
        with open(nome_arquivo, "r") as arquivo:
            while True:
                dado = arquivo.readline()
                if not dado:
                    break
                dado_lst.append(ast.literal_eval(dado))

        somaTotais = 0
        numReq = 0
        empresas, valores = [],[]

        # -------------------------------------------------------------
        # COLETA DE DADOS
        for info in dado_lst:
            numReq += 1
            somaTotais += info[4][0]
            numEmp = str(info[0][0]) + str(info[0][1]) + str(info[0][2]) + str(info[0][3]) + str(info[0][4]) + str(info[0][5]) + str(info[0][6]) + str(info[0][7]) + str(info[0][8]) + str(info[0][9]) + str(info[0][10]) + str(info[0][11]) + str(info[0][12])
            empresas.append(numEmp)
            valores.append(info[4][0])
        
        # -------------------------------------------------------------
        # COMPARAÇÕES E COMPARAÇÃO DE VARIÁVEIS

        mediaTotais = round(somaTotais/numReq,2)
        print(mediaTotais)

    # PLOTAGEM DE GRÁFICOS, A PARTIR DOS DADOS FILTRADOS
    # Gráfico de Barras de Erros dos custos, por cada setor
    matriz_bar = np.array([[financeiro_min,financeiro_medio,financeiro_max],[comercio_min,comercio_medio,comercio_max],[saude_min,saude_medio,saude_max]])
    minimos = np.min(matriz_bar, axis=1)
    medias = np.mean(matriz_bar, axis=1)
    maximos = np.max(matriz_bar, axis=1)
    erros_inferiores = [financeiro_min, comercio_min, saude_min]
    erros_superiores = [financeiro_max, comercio_max, saude_max]
    erros = [erros_inferiores, erros_superiores]
    labels = ['Financeiro', 'Comércio', 'Saúde']
    x = np.arange(len(labels))
    largura_barra = 0.35
    fig, ax = plt.subplots()
    barras = ax.bar(x, medias, largura_barra, yerr=erros, label='Empresas', capsize=2)
    ax.set_xlabel('Setor')
    ax.set_ylabel('Custo')
    ax.set_title('Custos Financeiros por Setor')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    for i in range(len(barras)):
        yval = barras[i].get_height()
        yerr_lower = erros_inferiores[i]
        yerr_upper = erros_superiores[i]
        ax.text(barras[i].get_x() + barras[i].get_width() / 2., yval,f'{yval:.2f}\n({yerr_lower:.2f}, {yerr_upper:.2f})',ha='center', va='bottom')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosSetores.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta,nome_imagem))
    plt.show()

    # Gráfico de Barras de Erros dos custos, por cada tipo de ataque
    matriz_bar = np.array([[malware_min,malware_medio,malware_max],[phishing_min,phishing_medio,phishing_max],[ddos_min,ddos_medio,ddos_max]])
    minimos = np.min(matriz_bar, axis=1)
    medias = np.mean(matriz_bar, axis=1)
    maximos = np.max(matriz_bar, axis=1)
    erros_inferiores = [malware_min, phishing_min, ddos_min]
    erros_superiores = [malware_max, phishing_max, ddos_max]
    erros = [erros_inferiores, erros_superiores]
    labels = ['Malware', 'Phishing', 'DDoS']
    x = np.arange(len(labels))
    largura_barra = 0.35
    fig, ax = plt.subplots()
    barras = ax.bar(x, medias, largura_barra, yerr=erros, label='Empresas', capsize=2)
    ax.set_xlabel('Ciberataque')
    ax.set_ylabel('Custo')
    ax.set_title('Custos Financeiros por Ciberataque')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    for i in range(len(barras)):
        yval = barras[i].get_height()
        yerr_lower = erros_inferiores[i]
        yerr_upper = erros_superiores[i]
        ax.text(barras[i].get_x() + barras[i].get_width() / 2., yval,f'{yval:.2f}\n({yerr_lower:.2f}, {yerr_upper:.2f})',ha='center', va='bottom')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosAtaques.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta,nome_imagem))
    plt.show()

    # Gráfico de Barras Agrupadas
    bar_width = 0.25
    x = np.arange(len(setores))
    plt.figure(figsize=(10, 6))
    plt.bar(x - bar_width, malware_media, width=bar_width, label='Malware', color='b')
    plt.bar(x, phishing_media, width=bar_width, label='Phishing', color='g')
    plt.bar(x + bar_width, ddos_media, width=bar_width, label='DDoS', color='r')
    plt.title('Distribuição de Porcentagens de Incidentes')
    plt.xlabel('Setores')
    plt.ylabel('Porcentagem (%)')
    plt.xticks(x, empresas)
    plt.ylim(0, 100)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()