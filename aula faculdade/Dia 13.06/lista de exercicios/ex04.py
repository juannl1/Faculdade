"""
🔹 4️⃣ Dicionário
Monte um dicionário para armazenar os dados de um produto:

Nome do produto

Preço

Quantidade em estoque
Depois, exiba os dados formatados e calcule o valor total do estoque do produto.
"""

produto = {
    "teclado": [19.90, 40]
}
soma = produto['teclado'][1] * produto['teclado'][0]
print(f"temos {produto['teclado'][1]} teclados que custam {produto['teclado'][0]}\nO valor total de estoque é {soma}")
