@echo off

REM Define a pasta onde estão os arquivos de entrada
set PASTA_ENTRADA=Gerador_Requisicoes

REM Loop para chamar o script Python com cada arquivo na pasta de entrada
for /l %%X in (0,1,316) do (
    python moduloSimulacoes.py %PASTA_ENTRADA%\req%%X.txt
)

echo Finalizado!
pause
