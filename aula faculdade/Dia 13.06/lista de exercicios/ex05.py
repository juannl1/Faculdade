"""
🔹 5️⃣ Laço com for e lista
Crie uma lista com quatro nomes. Use um for com enumerate para exibir:


1 - Nome1
2 - Nome2
"""

lista_nomes = ["Juan", "Caio", "Pedro", "João Victor"]

for c, nomes in enumerate(lista_nomes, start=1):
    print(f"{c}° Valor da lista é: {nomes}")
