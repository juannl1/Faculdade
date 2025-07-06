"""
🟣 5️⃣ Laço for com range e list
Crie um programa que gere uma lista com os quadrados dos números de 1 a 10. Depois:

Exiba os valores com for e enumerate, mostrando índice e valor.

Exiba a soma dos valores da lista.

"""
lista = []
for c in range(1, 11):
    n1 = int(input(f"{c}° Número: "))
    quadrado = n1 ** 2
    lista.append(quadrado)

for x, numeros in enumerate(lista, start=1):
    print(f"\n{x}° posição: {numeros}")

soma = sum(lista)
print(f"\nA soma dos números ficaram em: {soma}")