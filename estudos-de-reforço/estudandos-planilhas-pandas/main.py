"""
Anotações:

Dicionário --> DataFrame (Tabela) --> Arquivo Final 
"""


import pandas as pd

dados = {
    "id": 1,
    "nome": ["Juan", "Lemos"],
    "idade": 19,
    "detalhes": {
        "hobbie": "surf",
        "profissao": "J.A fiscal"
    }
}
df = pd.DataFrame(dados)

df.to_excel('base-de-dados.xlsx', index=False)


print(df)
