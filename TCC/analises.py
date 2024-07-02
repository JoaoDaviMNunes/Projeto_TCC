import os
import ast
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

setores = ['Financeiro','Comércio','Saúde']
ataques = ['Malware','Phishing','DDoS']
metricas = ['Mínimo','Média','Máximo']
divisor = 1000000       # para a plotagem de forma mais simplificada

def main():
    dado_lst = []

    # contador do número de requisições que possuem cada um dos tipos de ataque
    numM, numP, numD = 0,0,0
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
    numF, numC, numS = 0,0,0
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

    numSM, numSP, numSD = 0,0,0
    saude_malware_custos, saude_phishing_custos, saude_ddos_custos = 0,0,0
    saude_malware_min, saude_malware_media, saude_malware_max = 0,0,0
    saude_phishing_min, saude_phishing_media, saude_phishing_max = 0,0,0
    saude_ddos_min, saude_ddos_media, saude_ddos_max = 0,0,0

    # probabilidades
    financeiro_prob_malware, financeiro_prob_phishing, financeiro_prob_ddos = 0,0,0
    comercio_prob_malware, comercio_prob_phishing, comercio_prob_ddos = 0,0,0
    saude_prob_malware, saude_prob_phishing, saude_prob_ddos = 0,0,0
    npFM, npFP, npFD = 0,0,0
    npCM, npCP, npCD = 0,0,0
    npSM, npSP, npSD = 0,0,0
    financeiro_prob_media_malware, financeiro_prob_media_phishing, financeiro_prob_media_ddos = 0,0,0
    comercio_prob_media_malware, comercio_prob_media_phishing, comercio_prob_media_ddos = 0,0,0
    saude_prob_media_malware, saude_prob_media_phishing, saude_prob_media_ddos = 0,0,0

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

        # COLETA DE DADOS
        # info[0] = infos requisição
        # info[1] = infos malware
        # info[2] = infos phishing
        # info[3] = infos ddos
        # info[4] = infos custos
        for info in dado_lst:
            #print(info)
            numReq += 1
            somaTotais += info[4][0]
            numEmp = str(info[0][0]) + str(info[0][1]) + str(info[0][2]) + str(info[0][3]) + str(info[0][4]) + str(info[0][5]) + str(info[0][6]) + str(info[0][7]) + str(info[0][8]) + str(info[0][9]) + str(info[0][10]) + str(info[0][11]) + str(info[0][12])
            empresas.append(numEmp)
            valores.append(info[4][0])

            # pegando informações de malware --------------------------------
            if info[1][0] != 0 and info[0][3] == '1' and info[0][4] == '0' and info[0][5] == '0':
                numM += 1
                # baixo
                malware_baixo_custos += info[4][1]
                if malware_baixo_min == 0 and malware_baixo_max == 0:
                    malware_baixo_min, malware_baixo_max = info[4][1], info[4][1]
                elif info[4][1] < malware_baixo_min:
                    malware_baixo_min = info[4][1]
                elif info[4][1] > malware_baixo_max:
                    malware_baixo_max = info[4][1]
                # meio
                malware_meio_custos += info[4][0]
                if malware_meio_min == 0 and malware_meio_max == 0:
                    malware_meio_min, malware_meio_max = info[4][0], info[4][0]
                if info[4][0] < malware_meio_min:
                    malware_meio_min = info[4][0]
                if info[4][0] > malware_meio_max:
                    malware_meio_max = info[4][0]
                # alto
                malware_alto_custos += info[4][2]
                if malware_alto_min == 0 and malware_alto_max == 0:
                    malware_alto_min, malware_alto_max = info[4][2], info[4][2]
                if info[4][2] < malware_alto_min:
                    malware_alto_min = info[4][2]
                if info[4][2] > malware_alto_max:
                    malware_alto_max = info[4][2]

            # pegando informações de phishing --------------------------------
            if info[2][0] != 0 and info[0][3] == '0' and info[0][4] == '1' and info[0][5] == '0':
                numP += 1
                # baixo
                phishing_baixo_custos += info[4][1]
                if phishing_baixo_min == 0 and phishing_baixo_max == 0:
                    phishing_baixo_min, phishing_baixo_max = info[4][1], info[4][1]
                if info[4][1] < phishing_baixo_min:
                    phishing_baixo_min = info[4][1]
                if info[4][1] > phishing_baixo_max:
                    phishing_baixo_max = info[4][1]
                # meio
                phishing_meio_custos += info[4][0]
                if phishing_meio_min == 0 and phishing_meio_max == 0:
                    phishing_meio_min, phishing_meio_max = info[4][0], info[4][0]
                if info[4][0] < phishing_meio_min:
                    phishing_meio_min = info[4][0]
                if info[4][0] > phishing_meio_max:
                    phishing_meio_max = info[4][0]
                # alto
                phishing_alto_custos += info[4][2]
                if phishing_alto_min == 0 and phishing_alto_max == 0:
                    phishing_alto_min, phishing_alto_max = info[4][2], info[4][2]
                if info[4][2] < phishing_alto_min:
                    phishing_alto_min = info[4][2]
                if info[4][2] > phishing_alto_max:
                    phishing_alto_max = info[4][2]

            # pegando informações de DDoS --------------------------------
            if info[3][0] != 0 and info[0][3] == '0' and info[0][4] == '0' and info[0][5] == '1':
                numD += 1
                # baixo
                ddos_baixo_custos += info[4][1]
                if ddos_baixo_min == 0 and ddos_baixo_max == 0:
                    ddos_baixo_min, ddos_baixo_max = info[4][1], info[4][1]
                if info[4][1] < ddos_baixo_min:
                    ddos_baixo_min = info[4][1]
                if info[4][1] > ddos_baixo_max:
                    ddos_baixo_max = info[4][1]
                # meio
                ddos_meio_custos += info[4][0]
                if ddos_meio_min == 0 and ddos_meio_max == 0:
                    ddos_meio_min, ddos_meio_max = info[4][0], info[4][0]
                if info[4][0] < ddos_meio_min:
                    ddos_meio_min = info[4][0]
                if info[4][0] > ddos_meio_max:
                    ddos_meio_max = info[4][0]
                # alto
                ddos_alto_custos += info[4][2]
                if ddos_alto_min == 0 and ddos_alto_max == 0:
                    ddos_alto_min, ddos_alto_max = info[4][2], info[4][2]
                if info[4][2] < ddos_alto_min:
                    ddos_alto_min = info[4][2]
                if info[4][2] > ddos_alto_max:
                    ddos_alto_max = info[4][2]

            # pegando informações do setor financeiro --------------------------------
            if info[0][0] == '1':
                #print('Setor financeiro')
                numF += 1
                # baixo
                financeiro_baixo_custos += info[4][1]
                if financeiro_baixo_min == 0 and financeiro_baixo_max == 0:
                    financeiro_baixo_min, financeiro_baixo_max = info[4][1], info[4][1]
                if info[4][1] < financeiro_baixo_min:
                    financeiro_baixo_min = info[4][1]
                if info[4][1] > financeiro_baixo_max:
                    financeiro_baixo_max = info[4][1]
                # meio
                financeiro_meio_custos += info[4][0]
                if financeiro_meio_min == 0 and financeiro_meio_max == 0:
                    financeiro_meio_min, financeiro_meio_max = info[4][0], info[4][0]
                if info[4][0] < financeiro_meio_min:
                    financeiro_meio_min = info[4][0]
                if info[4][0] > financeiro_meio_max:
                    financeiro_meio_max = info[4][0]
                # alto
                financeiro_alto_custos += info[4][2]
                if financeiro_alto_min == 0 and financeiro_alto_max == 0:
                    financeiro_alto_min, financeiro_alto_max = info[4][2], info[4][2]
                if info[4][2] < financeiro_alto_min:
                    financeiro_alto_min = info[4][2]
                if info[4][2] > financeiro_alto_max:
                    financeiro_alto_max = info[4][2]
                
            # pegando informações do setor de comércio --------------------------------
            elif info[0][1] == '1':
                #print('Setor de comércio')
                numC += 1
                # baixo
                comercio_baixo_custos += info[4][1]
                if comercio_baixo_min == 0 and comercio_baixo_max == 0:
                    comercio_baixo_min, comercio_baixo_max = info[4][1], info[4][1]
                if info[4][1] < comercio_baixo_min:
                    comercio_baixo_min = info[4][1]
                if info[4][1] > comercio_baixo_max:
                    comercio_baixo_max = info[4][1]
                # meio
                comercio_meio_custos += info[4][0]
                if comercio_meio_min == 0 and comercio_meio_max == 0:
                    comercio_meio_min, comercio_meio_max = info[4][0], info[4][0]
                if info[4][0] < comercio_meio_min:
                    comercio_meio_min = info[4][0]
                if info[4][0] > comercio_meio_max:
                    comercio_meio_max = info[4][0]
                # alto
                comercio_alto_custos += info[4][2]
                if comercio_alto_min == 0 and comercio_alto_max == 0:
                    comercio_alto_min, comercio_alto_max = info[4][2], info[4][2]
                if info[4][2] < comercio_alto_min:
                    comercio_alto_min = info[4][2]
                if info[4][2] > comercio_alto_max:
                    comercio_alto_max = info[4][2]

            # pegando informações do setor de saúde --------------------------------
            elif info[0][2] == '1':
                #print('Setor de saúde')
                numS += 1
                # baixo
                saude_baixo_custos += info[4][1]
                if saude_baixo_min == 0 and saude_baixo_max == 0:
                    saude_baixo_min, saude_baixo_max = info[4][1], info[4][1]
                if info[4][1] < saude_baixo_min:
                    saude_baixo_min = info[4][1]
                if info[4][1] > saude_baixo_max:
                    saude_baixo_max = info[4][1]
                # meio
                saude_meio_custos += info[4][0]
                if saude_meio_min == 0 and saude_meio_max == 0:
                    saude_meio_min, saude_meio_max = info[4][0], info[4][0]
                if info[4][0] < saude_meio_min:
                    saude_meio_min = info[4][0]
                if info[4][0] > saude_meio_max:
                    saude_meio_max = info[4][0]
                # alto
                saude_alto_custos += info[4][2]
                if saude_alto_min == 0 and saude_alto_max == 0:
                    saude_alto_min, saude_alto_max = info[4][2], info[4][2]
                if info[4][2] < saude_alto_min:
                    saude_alto_min = info[4][2]
                if info[4][2] > saude_alto_max:
                    saude_alto_max = info[4][2]
                # malware
                if info[0][3] == '1' and info[0][4] == '0' and info[0][5] == '0':        # verificando se é malware
                    numSM += 1
                    saude_malware_custos += info[4][0]
                    if saude_malware_min == 0 and saude_malware_max == 0:
                        saude_malware_min, saude_malware_max = info[4][1], info[4][2]
                    if info[4][1] < saude_malware_min:
                        saude_malware_min = info[4][1]
                    if info[4][2] > saude_malware_max:
                        saude_malware_max = info[4][2]
                # phishing
                if info[0][3] == '0' and info[0][4] == '1' and info[0][5] == '0':        # verificando se é phishing
                    numSP += 1
                    saude_phishing_custos += info[4][0]
                    if saude_phishing_min == 0 and saude_phishing_max == 0:
                        saude_phishing_min, saude_phishing_max = info[4][1], info[4][2]
                    if info[4][1] < saude_phishing_min:
                        saude_phishing_min = info[4][1]
                    if info[4][2] > saude_phishing_max:
                        saude_phishing_max = info[4][2]
                # DDoS
                if info[0][3] == '0' and info[0][4] == '0' and info[0][5] == '1':        # verificando se é DDoS
                    numSD += 1
                    saude_ddos_custos += info[4][0]
                    if saude_ddos_min == 0 and saude_ddos_max == 0:
                        saude_ddos_min, saude_ddos_max = info[4][1], info[4][2]
                    if info[4][1] < saude_ddos_min:
                        saude_ddos_min = info[4][1]
                    if info[4][2] > saude_ddos_max:
                        saude_ddos_max = info[4][2]

            if info[0][0] == '1' and info[0][1] == '0' and info[0][2] == '0':
                # verificar se o ataque foi malware
                if info[0][3] == '1':
                    npFM += 1
                    financeiro_prob_malware += info[1][0]
                    #print('Financeiro - Malware - ' + str(info[1][0]))
                # verificar se o ataque foi phishing
                if info[0][4] == '1':
                    npFP += 1
                    financeiro_prob_phishing += info[2][0]
                    #print('Financeiro - Phishing - ' + str(info[2][0]))
                # verificar se o ataque foi DDoS
                if info[0][5] == '1':
                    npFD += 1
                    financeiro_prob_ddos += info[3][0]
                    #print('Financeiro - DDoS - ' + str(info[3][0]))
            if info[0][0] == '0' and info[0][1] == '1' and info[0][2] == '0':
                # verificar se o ataque foi malware
                if info[0][3] == '1':
                    npCM += 1
                    comercio_prob_malware += info[1][0]
                # verificar se o ataque foi phishing
                if info[0][4] == '1':
                    npCP += 1
                    comercio_prob_phishing += info[2][0]
                # verificar se o ataque foi DDoS
                if info[0][5] == '1':
                    npCD += 1
                    comercio_prob_ddos += info[3][0]
            if info[0][0] == '0' and info[0][1] == '0' and info[0][2] == '1':
                # verificar se o ataque foi malware
                if info[0][3] == '1':
                    npSM += 1
                    saude_prob_malware += info[1][0]
                # verificar se o ataque foi phishing
                if info[0][4] == '1':
                    npSP += 1
                    saude_prob_phishing += info[2][0]
                # verificar se o ataque foi DDoS
                if info[0][5] == '1':
                    npSD += 1
                    saude_prob_ddos += info[3][0]
        
    # -------------------------------------------------------------
    # CÁLCULO DAS MÉDIAS E COMPARAÇÃO DE VARIÁVEIS
    mediaCustos = round(somaTotais/numReq,2)

    malware_baixo_media = round(malware_baixo_custos/numM,2)
    malware_meio_media = round(malware_meio_custos/numM,2)
    malware_alto_media = round(malware_alto_custos/numM,2)
    phishing_baixo_media = round(phishing_baixo_custos/numP,2)
    phishing_meio_media = round(phishing_meio_custos/numP,2)
    phishing_alto_media = round(phishing_alto_custos/numP,2)
    ddos_baixo_media = round(ddos_baixo_custos/numD,2)
    ddos_meio_media = round(ddos_meio_custos/numD,2)
    ddos_alto_media = round(ddos_alto_custos/numD,2)
    
    financeiro_baixo_media = round(financeiro_baixo_custos/numF,2)
    financeiro_meio_media = round(financeiro_meio_custos/numF,2)
    financeiro_alto_media = round(financeiro_alto_custos/numF,2)
    comercio_baixo_media = round(comercio_baixo_custos/numC,2)
    comercio_meio_media = round(comercio_meio_custos/numC,2)
    comercio_alto_media = round(comercio_alto_custos/numC,2)
    saude_baixo_media = round(saude_baixo_custos/numS,2)
    saude_meio_media = round(saude_meio_custos/numS,2)
    saude_alto_media = round(saude_alto_custos/numS,2)

    saude_malware_media = round(saude_malware_custos/numSM,2)
    saude_phishing_media = round(saude_phishing_custos/numSP,2)
    saude_ddos_media = round(saude_ddos_custos/numSD,2)

    financeiro_prob_media_malware = round(financeiro_prob_malware/npFM,2)
    financeiro_prob_media_phishing = round(financeiro_prob_phishing/npFP,2)
    financeiro_prob_media_ddos = round(financeiro_prob_ddos/npFD,2)

    comercio_prob_media_malware = round(comercio_prob_malware/npCM,2)
    comercio_prob_media_phishing = round(comercio_prob_phishing/npCP,2)
    comercio_prob_media_ddos = round(comercio_prob_ddos/npCD,2)

    saude_prob_media_malware = round(saude_prob_malware/npSM,2)
    saude_prob_media_phishing = round(saude_prob_phishing/npSP,2)
    saude_prob_media_ddos = round(saude_prob_ddos/npSD,2)

    print(financeiro_prob_media_malware, financeiro_prob_media_phishing, financeiro_prob_media_ddos)
    print(comercio_prob_media_malware, comercio_prob_media_phishing, comercio_prob_media_ddos)
    print(saude_prob_media_malware, saude_prob_media_phishing, saude_prob_media_ddos)

    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # ------------------------------------- GRÁFICOS --------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    
    valores_medios = [financeiro_baixo_media, comercio_baixo_media, saude_baixo_media]
    valores_minimos = [financeiro_baixo_min, comercio_baixo_min, saude_baixo_min]
    valores_maximos = [financeiro_baixo_max, comercio_baixo_max, saude_baixo_max]
    erros_baixo = [media - minimo for media, minimo in zip(valores_medios, valores_minimos)]
    erros_cima = [maximo - media for media, maximo in zip(valores_medios, valores_maximos)]
    x = np.arange(len(setores))
    width = 0.5
    fig, ax = plt.subplots()
    bars = ax.bar(x, valores_medios, yerr=[erros_baixo, erros_cima], width=width, capsize=10, color='gray', edgecolor='black')
    ax.set_ylabel('Custos')
    ax.set_xlabel('Setores')
    ax.set_title('Gráfico de Barras com Erros')
    ax.set_xticks(x)
    ax.set_xticklabels(setores)
    for bar, media, minimo, maximo in zip(bars, valores_medios, valores_minimos, valores_maximos):
        height = bar.get_height()
        ax.annotate(f'{media}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento para cima
                    textcoords="offset points", ha='center', va='bottom', color='black')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosMinimoSetores.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    #plt.show()
    # -------------------------------------------------------------------------------------
    valores_medios = [malware_baixo_media, phishing_baixo_media, ddos_baixo_media]
    valores_minimos = [malware_baixo_min, phishing_baixo_min, ddos_baixo_min]
    valores_maximos = [malware_baixo_max, phishing_baixo_max, ddos_baixo_max]
    erros_baixo = [media - minimo for media, minimo in zip(valores_medios, valores_minimos)]
    erros_cima = [maximo - media for media, maximo in zip(valores_medios, valores_maximos)]
    x = np.arange(len(ataques))
    width = 0.5
    fig, ax = plt.subplots()
    bars = ax.bar(x, valores_medios, yerr=[erros_baixo, erros_cima], width=width, capsize=10, color='gray', edgecolor='black')
    ax.set_ylabel('Custos')
    ax.set_xlabel('Tipos de Ataques')
    ax.set_title('Gráfico de Barras com Erros')
    ax.set_xticks(x)
    ax.set_xticklabels(ataques)
    for bar, media, minimo, maximo in zip(bars, valores_medios, valores_minimos, valores_maximos):
        height = bar.get_height()
        ax.annotate(f'{media}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento para cima
                    textcoords="offset points", ha='center', va='bottom', color='black')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosMinimoAtaques.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    #plt.show()
    
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # DIVISÃO POR ALGUMA GRANDEZA (RAZÃO: NÚMEROS MUITO ALTOS E FEIOS PARA DEMONSTRAÇÃO)
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    mediaCustos = round(mediaCustos / divisor,2)

    malware_baixo_custos = round(malware_baixo_custos / divisor,2)
    phishing_baixo_custos = round(phishing_baixo_custos / divisor,2)
    ddos_baixo_custos = round(ddos_baixo_custos / divisor,2)
    malware_meio_custos = round(malware_meio_custos / divisor,2)
    phishing_meio_custos = round(phishing_meio_custos / divisor,2)
    ddos_meio_custos = round(ddos_meio_custos / divisor,2)
    malware_alto_custos = round(malware_alto_custos / divisor,2)
    phishing_alto_custos = round(phishing_alto_custos / divisor,2)
    ddos_alto_custos = round(ddos_alto_custos / divisor,2)
    malware_baixo_min = round(malware_baixo_min / divisor,2)
    malware_baixo_media = round(malware_baixo_media / divisor,2)
    malware_baixo_max = round(malware_baixo_max / divisor,2)
    malware_meio_min = round(malware_meio_min / divisor,2)
    malware_meio_media = round(malware_meio_media / divisor,2)
    malware_meio_max = round(malware_meio_max / divisor,2)
    malware_alto_min = round(malware_alto_min / divisor,2)
    malware_alto_media = round(malware_alto_media / divisor,2)
    malware_alto_max = round(malware_alto_max / divisor,2)
    phishing_baixo_min = round(phishing_baixo_min / divisor,2)
    phishing_baixo_media = round(phishing_baixo_media / divisor,2)
    phishing_baixo_max = round(phishing_baixo_max / divisor,2)
    phishing_meio_min = round(phishing_meio_min / divisor,2)
    phishing_meio_media = round(phishing_meio_media / divisor,2)
    phishing_meio_max = round(phishing_meio_max / divisor,2)
    phishing_alto_min = round(phishing_alto_min / divisor,2)
    phishing_alto_media = round(phishing_alto_media / divisor,2)
    phishing_alto_max = round(phishing_alto_max / divisor,2)
    ddos_baixo_min = round(ddos_baixo_min / divisor,2)
    ddos_baixo_media = round(ddos_baixo_media / divisor,2)
    ddos_baixo_max = round(ddos_baixo_max / divisor,2)
    ddos_meio_min = round(ddos_meio_min / divisor,2)
    ddos_meio_media = round(ddos_meio_media / divisor,2)
    ddos_meio_max = round(ddos_meio_max / divisor,2)
    ddos_alto_min = round(ddos_alto_min / divisor,2)
    ddos_alto_media = round(ddos_alto_media / divisor,2)
    ddos_alto_max = round(ddos_alto_max / divisor,2)

    financeiro_baixo_custos = round(financeiro_baixo_custos / divisor,2)
    comercio_baixo_custos = round(comercio_baixo_custos / divisor,2)
    saude_baixo_custos = round(saude_baixo_custos / divisor,2)
    financeiro_meio_custos = round(financeiro_meio_custos / divisor,2)
    comercio_meio_custos = round(comercio_meio_custos / divisor,2)
    saude_meio_custos = round(saude_meio_custos / divisor,2)
    financeiro_alto_custos = round(financeiro_alto_custos / divisor,2)
    comercio_alto_custos = round(comercio_alto_custos / divisor,2)
    saude_alto_custos = round(saude_alto_custos / divisor,2)
    financeiro_baixo_min = round(financeiro_baixo_min / divisor,2)
    financeiro_baixo_media = round(financeiro_baixo_media / divisor,2)
    financeiro_baixo_max = round(financeiro_baixo_max / divisor,2)     
    financeiro_meio_min = round(financeiro_meio_min / divisor,2)
    financeiro_meio_media = round(financeiro_meio_media / divisor,2)
    financeiro_meio_max = round(financeiro_meio_max / divisor,2)
    financeiro_alto_min = round(financeiro_alto_min / divisor,2)
    financeiro_alto_media = round(financeiro_alto_media / divisor,2)
    financeiro_alto_max = round(financeiro_alto_max / divisor,2)
    comercio_baixo_min = round(comercio_baixo_min / divisor,2)
    comercio_baixo_media = round(comercio_baixo_media / divisor,2)
    comercio_baixo_max = round(comercio_baixo_max / divisor,2)
    comercio_meio_min = round(comercio_meio_min / divisor,2)
    comercio_meio_media = round(comercio_meio_media / divisor,2)
    comercio_meio_max = round(comercio_meio_max / divisor,2)
    comercio_alto_min = round(comercio_alto_min / divisor,2)
    comercio_alto_media = round(comercio_alto_media / divisor,2)
    comercio_alto_max = round(comercio_alto_max / divisor,2)
    saude_baixo_min = round(saude_baixo_min / divisor,2)
    saude_baixo_media = round(saude_baixo_media / divisor,2)
    saude_baixo_max = round(saude_baixo_max / divisor,2)
    saude_meio_min = round(saude_meio_min / divisor,2)
    saude_meio_media = round(saude_meio_media / divisor,2)
    saude_meio_max = round(saude_meio_max / divisor,2)
    saude_alto_min = round(saude_alto_min / divisor,2)
    saude_alto_media = round(saude_alto_media / divisor,2)
    saude_alto_max = round(saude_alto_max / divisor,2)

    saude_malware_min = round(saude_malware_min / divisor,2)
    saude_phishing_min = round(saude_phishing_min / divisor,2)
    saude_ddos_min = round(saude_ddos_min / divisor,2)
    saude_malware_media = round(saude_malware_media / divisor,2)
    saude_phishing_media = round(saude_phishing_media / divisor,2)
    saude_ddos_media = round(saude_ddos_media / divisor,2)
    saude_malware_max = round(saude_malware_max / divisor,2)
    saude_phishing_max = round(saude_phishing_max / divisor,2)
    saude_ddos_max = round(saude_ddos_max / divisor,2)

    # -------------------------------------------------------------------------------------
    print("Fator de divisão: " + str(divisor))
    '''
    print("Custo médio: " + str(mediaCustos))
    print("---------------------------------------------------------")
    print("\nCusto (baixo) mínimo (setor financeiro): " + str(financeiro_baixo_min))
    print("Custo (baixo) médio (setor financeiro): " + str(financeiro_baixo_media))
    print("Custo (baixo) máximo (setor financeiro): " + str(financeiro_baixo_max))
    print("Custo (meio) mínimo (setor financeiro): " + str(financeiro_meio_min))
    print("Custo (meio) médio (setor financeiro): " + str(financeiro_meio_media))
    print("Custo (meio) máximo (setor financeiro): " + str(financeiro_meio_max))
    print("Custo (alto) mínimo (setor financeiro): " + str(financeiro_alto_min))
    print("Custo (alto) médio (setor financeiro): " + str(financeiro_alto_media))
    print("Custo (alto) máximo (setor financeiro): " + str(financeiro_alto_max))
    print("---------------------------------------------------------")
    print("\nCusto (baixo) mínimo (setor de comércio): " + str(comercio_baixo_min))
    print("Custo (baixo) médio (setor de comércio): " + str(comercio_baixo_media))
    print("Custo (baixo) máximo (setor de comércio): " + str(comercio_baixo_max))
    print("Custo (meio) mínimo (setor de comércio): " + str(comercio_meio_min))
    print("Custo (meio) médio (setor de comércio): " + str(comercio_meio_media))
    print("Custo (meio) máximo (setor de comércio): " + str(comercio_meio_max))
    print("Custo (alto) mínimo (setor de comércio): " + str(comercio_alto_min))
    print("Custo (alto) médio (setor de comércio): " + str(comercio_alto_media))
    print("Custo (alto) máximo (setor de comércio): " + str(comercio_alto_max))
    print("---------------------------------------------------------")
    print("\nCusto (baixo) mínimo (setor de saúde): " + str(saude_baixo_min))
    print("Custo (baixo) médio (setor de saúde): " + str(saude_baixo_media))
    print("Custo (baixo) máximo (setor de saúde): " + str(saude_baixo_max))
    print("Custo (meio) mínimo (setor de saúde): " + str(saude_meio_min))
    print("Custo (meio) médio (setor de saúde): " + str(saude_meio_media))
    print("Custo (meio) máximo (setor de saúde): " + str(saude_meio_max))
    print("Custo (alto) mínimo (setor de saúde): " + str(saude_alto_min))
    print("Custo (alto) médio (setor de saúde): " + str(saude_alto_media))
    print("Custo (alto) máximo (setor de saúde): " + str(saude_alto_max))
    print("---------------------------------------------------------")
    print("\nCusto (baixo) mínimo (malware): " + str(malware_baixo_min))
    print("Custo (baixo) médio (malware): " + str(malware_baixo_media))
    print("Custo (baixo) máximo (malware): " + str(malware_baixo_max))
    print("Custo (meio) mínimo (malware): " + str(malware_meio_min))
    print("Custo (meio) médio (malware): " + str(malware_meio_media))
    print("Custo (meio) máximo (malware): " + str(malware_meio_max))
    print("Custo (alto) mínimo (malware): " + str(malware_alto_min))
    print("Custo (alto) médio (malware): " + str(malware_alto_media))
    print("Custo (alto) máximo (malware): " + str(malware_alto_max))
    print("---------------------------------------------------------")
    print("\nCusto (baixo) mínimo (phishing): " + str(phishing_baixo_min))
    print("Custo (baixo) médio (phishing): " + str(phishing_baixo_media))
    print("Custo (baixo) máximo (phishing): " + str(phishing_baixo_max))
    print("Custo (meio) mínimo (phishing): " + str(phishing_meio_min))
    print("Custo (meio) médio (phishing): " + str(phishing_meio_media))
    print("Custo (meio) máximo (phishing): " + str(phishing_meio_max))
    print("Custo (alto) mínimo (phishing): " + str(phishing_alto_min))
    print("Custo (alto) médio (phishing): " + str(phishing_alto_media))
    print("Custo (alto) máximo (phishing): " + str(phishing_alto_max))
    print("---------------------------------------------------------")
    print("Custo (baixo) mínimo (DDoS): " + str(ddos_baixo_min))
    print("Custo (baixo) médio (DDoS): " + str(ddos_baixo_media))
    print("Custo (baixo) máximo (DDoS): " + str(ddos_baixo_max))
    print("Custo (meio) mínimo (DDoS): " + str(ddos_meio_min))
    print("Custo (meio) médio (DDoS): " + str(ddos_meio_media))
    print("Custo (meio) máximo (DDoS): " + str(ddos_meio_max))
    print("Custo (alto) mínimo (DDoS): " + str(ddos_alto_min))
    print("Custo (alto) médio (DDoS): " + str(ddos_alto_media))
    print("Custo (alto) máximo (DDoS): " + str(ddos_alto_max))
    print("---------------------------------------------------------")
    '''
    # -----------------------------------------------------------------------------------------------------
    valores_medios = [financeiro_meio_media, comercio_meio_media, saude_meio_media]
    valores_minimos = [financeiro_meio_min, comercio_meio_min, saude_meio_min]
    valores_maximos = [financeiro_meio_max, comercio_meio_max, saude_meio_max]
    erros_baixo = [media - minimo for media, minimo in zip(valores_medios, valores_minimos)]
    erros_cima = [maximo - media for media, maximo in zip(valores_medios, valores_maximos)]
    x = np.arange(len(setores))
    width = 0.5
    fig, ax = plt.subplots()
    bars = ax.bar(x, valores_medios, yerr=[erros_baixo, erros_cima], width=width, capsize=10, color='gray', edgecolor='black')
    ax.set_ylabel('Custos (em milhões de dólares)')
    ax.set_xlabel('Setores')
    ax.set_title('Gráfico de Barras com Erros')
    ax.set_xticks(x)
    ax.set_xticklabels(setores)
    for bar, media, minimo, maximo in zip(bars, valores_medios, valores_minimos, valores_maximos):
        height = bar.get_height()
        ax.annotate(f'{media}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento para cima
                    textcoords="offset points", ha='center', va='bottom', color='black')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    os.makedirs(caminho_pasta, exist_ok=True)
    nome_imagem_png = 'custosMediaSetores.png'
    nome_imagem_pdf = 'custosMediaSetores.pdf'
    plt.savefig(os.path.join(caminho_pasta, nome_imagem_png))
    plt.savefig(os.path.join(caminho_pasta, nome_imagem_pdf))
    plt.show()
    # -----------------------------------------------------------------------------------------------------
    
    valores_medios = [financeiro_alto_media, comercio_alto_media, saude_alto_media]
    valores_minimos = [financeiro_alto_min, comercio_alto_min, saude_alto_min]
    valores_maximos = [financeiro_alto_max, comercio_alto_max, saude_alto_max]
    erros_baixo = [media - minimo for media, minimo in zip(valores_medios, valores_minimos)]
    erros_cima = [maximo - media for media, maximo in zip(valores_medios, valores_maximos)]
    x = np.arange(len(setores))
    width = 0.5
    fig, ax = plt.subplots()
    bars = ax.bar(x, valores_medios, yerr=[erros_baixo, erros_cima], width=width, capsize=10, color='gray', edgecolor='black')
    ax.set_ylabel('Valores (em milhões de dólares)')
    ax.set_xlabel('Setores')
    ax.set_title('Gráfico de Barras com Erros')
    ax.set_xticks(x)
    ax.set_xticklabels(setores)
    for bar, media, minimo, maximo in zip(bars, valores_medios, valores_minimos, valores_maximos):
        height = bar.get_height()
        ax.annotate(f'{media}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento para cima
                    textcoords="offset points", ha='center', va='bottom', color='black')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosMaximoSetores.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    plt.show()
    
    # -----------------------------------------------------------------------------------------------------
    valores_medios = [malware_meio_media, phishing_meio_media, ddos_meio_media]
    valores_minimos = [malware_meio_min, phishing_meio_min, ddos_meio_min]
    valores_maximos = [malware_meio_max, phishing_meio_max, ddos_meio_max]
    erros_baixo = [media - minimo for media, minimo in zip(valores_medios, valores_minimos)]
    erros_cima = [maximo - media for media, maximo in zip(valores_medios, valores_maximos)]
    x = np.arange(len(ataques))
    width = 0.5
    fig, ax = plt.subplots()
    bars = ax.bar(x, valores_medios, yerr=[erros_baixo, erros_cima], width=width, capsize=10, color='gray', edgecolor='black')
    ax.set_ylabel('Custos (em milhões de dólares)')
    ax.set_xlabel('Tipos de Ataques')
    ax.set_title('Gráfico de Barras com Erros')
    ax.set_xticks(x)
    ax.set_xticklabels(ataques)
    for bar, media, minimo, maximo in zip(bars, valores_medios, valores_minimos, valores_maximos):
        height = bar.get_height()
        ax.annotate(f'{media}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento para cima
                    textcoords="offset points", ha='center', va='bottom', color='black')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    os.makedirs(caminho_pasta, exist_ok=True)
    nome_imagem_png = 'custosMediaAtaques.png'
    nome_imagem_pdf = 'custosMediaAtaques.pdf'
    plt.savefig(os.path.join(caminho_pasta, nome_imagem_png))
    plt.savefig(os.path.join(caminho_pasta, nome_imagem_pdf))
    plt.show()
    # -----------------------------------------------------------------------------------------------------
    
    valores_medios = [malware_alto_media, phishing_alto_media, ddos_alto_media]
    valores_minimos = [malware_alto_min, phishing_alto_min, ddos_alto_min]
    valores_maximos = [malware_alto_max, phishing_alto_max, ddos_alto_max]
    erros_baixo = [media - minimo for media, minimo in zip(valores_medios, valores_minimos)]
    erros_cima = [maximo - media for media, maximo in zip(valores_medios, valores_maximos)]
    x = np.arange(len(ataques))
    width = 0.5
    fig, ax = plt.subplots()
    bars = ax.bar(x, valores_medios, yerr=[erros_baixo, erros_cima], width=width, capsize=10, color='gray', edgecolor='black')
    ax.set_ylabel('Valores (em milhões de dólares)')
    ax.set_xlabel('Tipos de Ataques')
    ax.set_title('Gráfico de Barras com Erros')
    ax.set_xticks(x)
    ax.set_xticklabels(ataques)
    for bar, media, minimo, maximo in zip(bars, valores_medios, valores_minimos, valores_maximos):
        height = bar.get_height()
        ax.annotate(f'{media}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', color='black')
    plt.tight_layout()
    caminho_pasta = "./Imagens"
    nome_imagem = 'custosMaximoAtaques.png'
    os.makedirs(caminho_pasta, exist_ok=True)
    plt.savefig(os.path.join(caminho_pasta, nome_imagem))
    plt.show()
    
    # -----------------------------------------------------------------------------------------------------
    plotdata = pd.DataFrame({
        "Malware":[saude_malware_media,saude_malware_max],
        "Phishing":[saude_phishing_media, saude_phishing_max],
        "DDoS":[saude_ddos_media, saude_ddos_max]},
        index=["Médias", "Máximos"])

    fig, ax = plt.subplots(figsize=(15, 8))  # Ajuste do tamanho da figura
    plotdata.plot(kind="bar", ax=ax, width=0.8, color=['#333333', '#666666', '#999999'])  # Ajuste do espaçamento entre as barras
    plt.title("Setor de Saúde: Ataque vs Custo")
    plt.xlabel("Tipos de ataques")
    plt.ylabel("Custos (em milhões de dólares)")
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    caminho_pasta = "./Imagens"
    os.makedirs(caminho_pasta, exist_ok=True)
    nome_imagem_png = 'custosAtaquesSaudeBarras.png'
    nome_imagem_pdf = 'custosAtaquesSaudeBarras.pdf'
    plt.savefig(os.path.join(caminho_pasta, nome_imagem_png))
    plt.savefig(os.path.join(caminho_pasta, nome_imagem_pdf))
    plt.show()
    
    pass

if __name__ == "__main__":
    main()