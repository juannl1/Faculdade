import pandas as pd
import os

# 1. Configuração de caminhos e criação da pasta
caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
pasta_banco = os.path.join(caminho_da_pasta, 'banco-de-dados')

if not os.path.exists(pasta_banco):
    os.makedirs(pasta_banco)

caminho_final = os.path.join(pasta_banco, 'base-de-dados-form.csv')

# 2. Dados
dados_form = {
    "id-do-registro": [1],
    "data": ["17/01"],
    "hora_da_anotacao": ["21:18"],
    "matrícula_do_fiscal": [11175],
    "número_da_linha": ["2146D"],
    "ponto_de_controle": ["Estação merçes"],
    "número_do_carro": [78],
    "matrícula_do_motorista": [9774],
    "hora_de_chegada": ["9:00"],
    "hora_de_saida": ["10:21"],
    "tempo_de_viagem": ["1:21"],
    "roleta_inicial": [90100],
    "roleta_local": [90147]
}

df = pd.DataFrame(dados_form)

# 3. SALVAR COM OS AJUSTES PARA EXCEL BRASIL
# Importante: se você for ler com o pandas depois, lembre de avisar que o separador agora é ';'
df.to_csv(
    caminho_final, 
    mode="a", 
    index=False, 
    header=not os.path.exists(caminho_final), 
    sep=';',           # <-- Resolve o problema das colunas grudadas
    encoding="utf-8-sig" # <-- Resolve o problema dos acentos (Ç, Ã, Ê)
)

print(f"Dados registrados com sucesso!")

# 4. LER DE VOLTA (Avisando que o separador é ';')
if os.path.exists(caminho_final):
    df_completo = pd.read_csv(caminho_final, sep=';', encoding="utf-8-sig")
    print(df_completo)