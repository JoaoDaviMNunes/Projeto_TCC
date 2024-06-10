import sys
import ast
import matplotlib.pyplot as plt
import numpy as np

def main():
    dado_lst = []
    with open("resultados.txt", "r") as arquivo:
        while True:
            dado = arquivo.readline()
            if not dado:
                break
            dado_lst.append(ast.literal_eval(dado))
    
    somaTotais = 0
    numReq = 0
    empresas, valores = [],[]

    for info in dado_lst:
        numReq += 1
        somaTotais += info[4][0]
        numEmp = info[0][0] + info[0][1] + info[0][2] + info[0][3] + info[0][4] + info[0][5] + info[0][6] + info[0][7] + info[0][8] + info[0][9] + info[0][10] + info[0][11] + info[0][12]
        empresas.append(numEmp)
        valores.append(info[4][0])

    mediaTotais = round(somaTotais/numReq,2)
    print(mediaTotais)

    # Plotar o gráfico de linha
    plt.plot(empresas, valores, marker='o', linestyle='-', color='b')

    # Adicionar título e rótulos aos eixos
    plt.title('Valores das Empresas')
    plt.xlabel('Empresas')
    plt.ylabel('Valores')

    # Exibir o gráfico
    plt.show()

if __name__ == "__main__":
    main()