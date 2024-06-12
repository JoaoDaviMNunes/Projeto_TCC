import sys
import os
import ast
import matplotlib.pyplot as plt
import numpy as np

setores = ['Financeiro','Comércio','Saúde']
ataques = ['Malware','Phishing','DDoS']

def main():
    dado_lst = []

    # contador do número de requisições que possuem cada um dos tipos de ataque
    numM_min, numP_min, numD_min = 0,0,0
    numM_media, numP_media, numD_media = 0,0,0
    numM_max, numP_max, numD_max = 0,0,0
    # acumulador de custos de cada tipo de ataque
    malware_baixo_custos, phishing_baixo_custos, ddos_baixo_custos = 0,0,0
    malware_meio_custos, phishing_meio_custos, ddos_meio_custos = 0,0,0
    malware_alto_custos, phishing_alto_custos, ddos_alto_custos = 0,0,0
    # probabilidades mínima, média e máxima de malware
    malware_baixo_min,malware_baixo_media,malware_baixo_max = 0,0,0
    malware_meio_min,malware_meio_media,malware_meio_max = 0,0,0
    malware_alto_min,malware_alto_media,malware_alto_max = 0,0,0
    phishing_baixo_min,phishing_baixo_media,phishing_baixo_max = 0,0,0
    phishing_meio_min,phishing_meio_media,phishing_meio_max = 0,0,0
    phishing_alto_min,phishing_alto_media,phishing_alto_max = 0,0,0
    ddos_baixo_min,ddos_baixo_media,ddos_baixo_max = 0,0,0
    ddos_meio_min,ddos_meio_media,ddos_meio_max = 0,0,0
    ddos_alto_min,ddos_alto_media,ddos_alto_max = 0,0,0

    # contador do número de requisições que possuem cada um dos setores
    numF_min, numC_min, numS_min = 0,0,0
    numF_media, numC_media, numS_media = 0,0,0
    numF_max, numC_max, numS_max = 0,0,0
    # acumulador de custos de cada setor
    financeiro_baixo_custos, comercio_baixo_custos, saude_baixo_custos = 0,0,0      
    financeiro_meio_custos, comercio_meio_custos, saude_meio_custos = 0,0,0
    financeiro_alto_custos, comercio_alto_custos, saude_alto_custos = 0,0,0
    # probabilidades mínima, média e máxima do setor financeiro
    financeiro_baixo_min,financeiro_baixo_media,financeiro_baixo_max = 0,0,0        
    financeiro_meio_min,financeiro_meio_media,financeiro_meio_max = 0,0,0
    financeiro_alto_min,financeiro_alto_media,financeiro_alto_max = 0,0,0
    comercio_baixo_min,comercio_baixo_media,comercio_baixo_max = 0,0,0
    comercio_meio_min,comercio_meio_media,comercio_meio_max = 0,0,0
    comercio_alto_min,comercio_alto_media,comercio_alto_max = 0,0,0
    saude_baixo_min,saude_baixo_media,saude_baixo_max = 0,0,0
    saude_meio_min,saude_meio_media,saude_meio_max = 0,0,0
    saude_alto_min,saude_alto_media,saude_alto_max = 0,0,0

    for i in range(100):    
        nome_arquivo = "./ResultadosCompletos/rodada" + str(i) + ".txt"
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
        # info[0] = infos requisição
        # info[1] = infos malware
        # info[2] = infos phishing
        # info[3] = infos ddos
        # info[4] = infos custos
        # COLETA DE DADOS
        for info in dado_lst:
            #print(info)
            numReq += 1
            somaTotais += info[4][0]
            numEmp = str(info[0][0]) + str(info[0][1]) + str(info[0][2]) + str(info[0][3]) + str(info[0][4]) + str(info[0][5]) + str(info[0][6]) + str(info[0][7]) + str(info[0][8]) + str(info[0][9]) + str(info[0][10]) + str(info[0][11]) + str(info[0][12])
            empresas.append(numEmp)
            valores.append(info[4][0])

            # pegando informações de malware
            if info[1][0] != 0 and info[0][3] == '1' and info[0][4] == '0' and info[0][5] == '0':
                numM += 1
                malware_custos += info[4][0]
                if malware_min == 0 and malware_max == 0:
                    malware_min, malware_max = info[4][1], info[4][2]
                if info[4][1] < malware_min:
                    malware_min = info[4][1]
                if info[4][2] > malware_max:
                    malware_max = info[4][2]

            # pegando informações de phishing
            if info[2][0] != 0 and info[0][3] == '0' and info[0][4] == '1' and info[0][5] == '0':
                numP += 1
                phishing_custos += info[4][0]
                if phishing_min == 0 and phishing_max == 0:
                    phishing_min, phishing_max = info[4][1], info[4][2]
                if info[4][1] < phishing_min:
                    phishing_min = info[4][1]
                if info[4][2] > phishing_max:
                    phishing_max = info[4][2]

            # pegando informações de DDoS
            if info[3][0] != 0 and info[0][3] == '0' and info[0][4] == '0' and info[0][5] == '1':
                numD += 1
                ddos_custos += info[4][0]
                if ddos_min == 0 and ddos_max == 0:
                    ddos_min, ddos_max = info[4][1], info[4][2]
                if info[4][1] < ddos_min:
                    ddos_min = info[4][1]
                if info[4][2] > ddos_max:
                    ddos_max = info[4][2]

            # pegando informações do setor financeiro
            if info[0][0] == '1':
                #print('Setor financeiro')
                numF += 1
                financeiro_custos += info[4][0]
                if financeiro_min == 0 and financeiro_max == 0:
                    financeiro_min, financeiro_max = info[4][1], info[4][2]
                if info[4][1] < financeiro_min:
                    financeiro_min = info[4][1]
                if info[4][2] > financeiro_max:
                    financeiro_max = info[4][2]
            elif info[0][1] == '1':
                #print('Setor de comércio')
                numC += 1
                comercio_custos += info[4][0]
                if comercio_min == 0 and comercio_max == 0:
                    comercio_min, comercio_max = info[4][1], info[4][2]
                if info[4][1] < comercio_min:
                    comercio_min = info[4][1]
                if info[4][2] > comercio_max:
                    comercio_max = info[4][2]
            elif info[0][2] == '1':
                #print('Setor de saúde')
                numS += 1
                saude_custos += info[4][0]
                if saude_min == 0 and saude_max == 0:
                    saude_min, saude_max = info[4][1], info[4][2]
                if info[4][1] < saude_min:
                    saude_min = info[4][1]
                if info[4][2] > saude_max:
                    saude_max = info[4][2]
        
    # -------------------------------------------------------------
    # CÁLCULO DAS MÉDIAS E COMPARAÇÃO DE VARIÁVEIS
    mediaCustos = round(somaTotais/numReq,2)
    malware_media = round(malware_custos/numM,2)
    phishing_media = round(phishing_custos/numP,2)
    ddos_media = round(ddos_custos/numD,2)
    financeiro_media = round(financeiro_custos/numF,2)
    comercio_media = round(comercio_custos/numC,2)
    saude_media = round(saude_custos/numS,2)
    
    print("Custo médio: " + str(mediaCustos))

    print("\nCusto mínimo (setor financeiro): " + str(financeiro_min))
    print("Custo médio (setor financeiro): " + str(financeiro_media))
    print("Custo máximo (setor financeiro): " + str(financeiro_max))
    print("\nCusto mínimo (setor de comércio): " + str(comercio_min))
    print("Custo médio (setor de comércio): " + str(comercio_media))
    print("Custo máximo (setor de comércio): " + str(comercio_max))
    print("\nCusto mínimo (setor de saúde): " + str(saude_min))
    print("Custo médio (setor de saúde): " + str(saude_media))
    print("Custo máximo (setor de saúde): " + str(saude_max))

    print("Custo mínimo (malware): " + str(malware_min))
    print("Custo médio (malware): " + str(malware_media))
    print("Custo máximo (malware): " + str(malware_max))
    print("\nCusto mínimo (phishing): " + str(phishing_min))
    print("Custo médio (phishing): " + str(phishing_media))
    print("Custo máximo (phishing): " + str(phishing_max))
    print("\nCusto mínimo (DDoS): " + str(ddos_min))
    print("Custo médio (DDoS): " + str(ddos_media))
    print("Custo máximo (DDoS): " + str(ddos_max))
    
    '''
    # PLOTAGEM DE GRÁFICOS, A PARTIR DOS DADOS FILTRADOS
    # Gráfico de Barras de Erros dos custos, por cada setor
    matriz_bar = np.array([[financeiro_min,financeiro_media,financeiro_max],[comercio_min,comercio_media,comercio_max],[saude_min,saude_media,saude_max]])
    minimos = np.min(matriz_bar, axis=1)
    medias = np.mean(matriz_bar, axis=1)
    maximos = np.max(matriz_bar, axis=1)
    erros_inferiores = medias - minimos
    erros_superiores = maximos - medias
    erros = [erros_inferiores, erros_superiores]
    labels = ['Financeiro', 'Comércio', 'Saúde']
    x = np.arange(len(labels))
    largura_barra = 0.35
    fig, ax = plt.subplots()
    barras = ax.bar(x, medias, largura_barra, yerr=erros, label='Empresas', capsize=5)
    ax.set_xlabel('Setor')
    ax.set_ylabel('Custo')
    ax.set_title('Custos Financeiros por Setor')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_ylim(0, max(maximos) * 1.1)
    for i in range(len(barras)):
        yval = barras[i].get_height()
        yerr_lower = erros_inferiores[i]
        yerr_upper = erros_superiores[i]
        ax.text(barras[i].get_x() + barras[i].get_width() / 2., yval,
                f'{yval:.2f}\n({yerr_lower:.2f}, {yerr_upper:.2f})', ha='center', va='bottom')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosSetores.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    plt.show()

    # Gráfico de Barras de Erros dos custos, por cada tipo de ataque
    matriz_bar = np.array([[malware_min,malware_media,malware_max],[phishing_min,phishing_media,phishing_max],[ddos_min,ddos_media,ddos_max]])
    minimos = np.min(matriz_bar, axis=1)
    medias = np.mean(matriz_bar, axis=1)
    maximos = np.max(matriz_bar, axis=1)
    erros_inferiores = medias - minimos
    erros_superiores = maximos - medias
    erros = [erros_inferiores, erros_superiores]
    labels = ['Malware', 'Phishing', 'DDoS']
    x = np.arange(len(labels))
    largura_barra = 0.35
    fig, ax = plt.subplots()
    barras = ax.bar(x, medias, largura_barra, yerr=erros, label='Empresas', capsize=5)
    ax.set_xlabel('Ciberataque')
    ax.set_ylabel('Custo')
    ax.set_title('Custos Financeiros por Ciberataque')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_ylim(0, max(maximos) * 1.1)
    for i in range(len(barras)):
        yval = barras[i].get_height()
        yerr_lower = erros_inferiores[i]
        yerr_upper = erros_superiores[i]
        ax.text(barras[i].get_x() + barras[i].get_width() / 2., yval,
                f'{yval:.2f}\n({yerr_lower:.2f}, {yerr_upper:.2f})', ha='center', va='bottom')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosAtaques.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    plt.show()

    # Gráfico de Barras Agrupadas
    bar_width = 0.25
    r1 = np.arange(len(setores))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    plt.figure(figsize=(10, 6))
    plt.bar(r1, malware_media, color='b', width=bar_width, edgecolor='grey', label='Malware')
    plt.bar(r2, phishing_media, color='g', width=bar_width, edgecolor='grey', label='Phishing')
    plt.bar(r3, ddos_media, color='r', width=bar_width, edgecolor='grey', label='DDoS')
    plt.xlabel('Setores', fontweight='bold')
    plt.ylabel('Custo Médio', fontweight='bold')
    plt.title('Custos Médios por Ciberataque em Diferentes Setores')
    plt.xticks([r + bar_width for r in range(len(setores))], setores)
    plt.legend()
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosAgrupados.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    plt.show()
    '''

if __name__ == "__main__":
    main()