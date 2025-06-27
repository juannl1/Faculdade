"""
🟡 1️⃣ Listas — Manipulação e Cálculo
Peça ao usuário para digitar 6 números e armazene-os em uma lista. Depois:

Exiba a média dos números.

Exiba os números em ordem crescente.

Exiba apenas os números pares da lista.
"""


lista = []
for c in range(1, 6):
    n1 = int(input(f"Digite o {c}° valor: "))
    lista.append(n1)

print(f"Sua lista: {lista}")

media = (sum(lista)) / 2
print(f"A média dos números é: {media}")

ordem_crescente = sorted(lista)
ordem_decrescente = sorted(lista, reverse=True)
numeros_pares = lista

print(f"Em ordem crescente: {ordem_crescente}")
print(f"Em ordem decrescente: {ordem_decrescente}")

