"""
Crie uma lista com cinco números digitados pelo usuário. Depois:

Exiba a soma desses números.


Exiba o maior e o menor número
"""

print("Faça uma lista de números")

lista = []
for x in range (1, 5 + 1):
    n1 = int(input(f"Digite {x}° valor: "))
    lista.append(n1)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(f"lista = {lista}")
print(f"A soma desses números é = {soma}")
print(f"O menor valor dessa lista é = {menor}\nE o maior valor é = {maior}")
