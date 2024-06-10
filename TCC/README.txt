FORMATO DA REQUISIÇÃO

# ------------------------------------------------------------------
# EXPLICAÇÃO

valores com campos são apenas 0 e 1
0 indica ausência de tal informação
1 indica presença de tal informação

# Apenas um campo pode ser acionado
# [0] = primeiro campo indica que o setor da empresa é o Financeiro
# [1] = segundo campo indica que o setor da empresa é o Saúde
# [2] = terceiro campo indica que o setor da empresa é o Comércio
setor = 111

# [0] = primeiro campo indica que o tipo de ataque buscado é Malware
# [1] = segundo campo indica que o tipo de ataque buscado é Phishing
# [2] = terceiro campo indica que o tipo de ataque buscado é DDoS
tpataque = 111

# [0] = primeiro campo indica que o local da empresa é APAC
# [1] = segundo campo indica que o local da empresa é LATAM
# [2] = terceiro campo indica que o local da empresa é EMEA
# [3] = quarto campo indica que o local da empresa é NA
local = 1111

# Apenas um campo pode ser acionado
# [0] = primeiro campo indica que busca qualquer tipo de dado no Banco de Dados
# [1] = segundo campo indica que busca dados de empresa relevantes ou muito relevantes no Banco de Dados
# [2] = terceiro campo indica que busca dados de empresas muito relevantes no Banco de Dados
classifDados = 111

# ------------------------------------------------------------------
# EXEMPLO
100
110
100000
110

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
DADOS DE ENTRADA (RELATÓRIOS, ESTATÍSTICAS, CURADORES, CONSULTORES) (14 campos)
[empresa,ano,avaliação,infoA,infoB,dadoA,dadoAB,referencia,reputacao,periodicidade,cobertura,escopo,abrangencia,metodologia]
empresa = [0]
ano = [1]
avaliação = [2]
infoA = [3]
infoB = [4]
dadoA = [5]
dadoAB = [6]
referencia = [7]
reputacao = [8]
periodicidade = [9]
cobertura = [10]
escopo = [11]
abrangencia = [12]
metodologia = [13]


