#!/bin/bash

# Definir a pasta de entrada
pasta_entrada="Gerador_Requisicoes"

# Loop para chamar o script Python com cada arquivo na pasta de entrada
for arquivo in "$pasta_entrada"/req*.txt; do
    python3 moduloSimulacoes.py "$arquivo"
done

echo "Finalizado!"