FORMATO DA REQUISIÇÃO

# ------------------------------------------------------------------
# EXPLICAÇÃO

valores com campos são apenas 0 e 1

# [0] = primeiro campo indica que o setor da empresa é o Financeiro
# [1] = segundo campo indica que o setor da empresa é o Saúde
# [2] = terceiro campo indica que o setor da empresa é o Comércio
setor = [1,1,1]

# [0] = primeiro campo indica que o tipo de ataque buscado é Malware
# [1] = segundo campo indica que o tipo de ataque buscado é Phishing
# [2] = terceiro campo indica que o tipo de ataque buscado é DDoS
tpataque = [1,1,1]

# [0] = primeiro campo indica que o local da empresa é América do Sul
# [1] = segundo campo indica que o local da empresa é América do Norte
# [2] = terceiro campo indica que o local da empresa é Europa
# [3] = quarto campo indica que o local da empresa é Ásia
# [4] = quinto campo indica que o local da empresa é Oceania
# [5] = sexto campo indica que o local da empresa é África
local = [1,1,1,1,1,1]

# [0] = primeiro campo indica que a empresa possui o ativo de uso de nuvem
# [1] = segundo campo indica que a empresa possui o ativo de firewall
# [2] = terceiro campo indica que a empresa possui o ativo de acesso remoto
# [3] = quarto campo indica que a empresa possui o ativo de
# [4] = quinto campo indica que a empresa possui o ativo de
# [5] = sexto campo indica que a empresa possui o ativo de
ativos = [1,1,1,1,1,1]

# ------------------------------------------------------------------
# EXEMPLO
setor=[1,0,0]
tpataque=[1,1,0]
local=[1,0,0,0,0,0]
ativos=[1,1,0,0,1,0]

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
DADOS DE ENTRADA (RELATÓRIOS, ESTATÍSTICAS, CURADORES, CONSULTORES) (14 campos)
[empresa,ano,avaliação,infoA,infoB,dadoA,dadoAB,fonte,reputacao,periodicidade,cobertura,escopo,abrangencia,metodologia]


