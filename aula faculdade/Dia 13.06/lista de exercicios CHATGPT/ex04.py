"""
🟠 4️⃣ Dicionário — Dados pessoais
Crie um dicionário com os seguintes dados de uma pessoa:

Nome

Idade

Profissão

Salário

Depois:

Mostre os dados formatados.

Aumente o salário em 10% e mostre o novo valor.

Verifique se a chave "endereço" existe no dicionário.
"""


infos = {
    'nome1':['Juan Dos Anjos Lemos', 18, "Auxíliar de Tráfego (Jovem Aprendiz)", 660]
}
print(f"Nome: {infos['nome1'][0]}\nIdade: {infos['nome1'][1]}\nProfissão: {infos['nome1'][2]}\nSalário: R$ {infos['nome1'][3]:.2f}")


aumento = (infos['nome1'][3] * 0.10) + infos['nome1'][3]

print(f"O user: {infos['nome1'][0]} recebeu um aumento de 10% no sálario")
print(f"Sálario atualizado: R$ {aumento:.2f}")
