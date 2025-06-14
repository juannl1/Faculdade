"""
🔹 2️⃣ Tuplas
Crie uma Tupla com três coordenadas (x, y, z) informadas pelo usuário. Depois:

Exiba as coordenadas separadamente (uma por linha).

Mostre o valor da coordenada y.
"""

print("Coordernadas\n")
tupla = ()
lista = list(tupla)

for c in range(1, 4):
    n1 = int(input(f"Digite o {c}° valor:  "))
    lista.append(n1)
tupla_atualizada = tuple(lista)
print(tupla_atualizada)
print(f"X = {tupla_atualizada[0]}")
print(f"Y = {tupla_atualizada[1]}")
print(f"Z = {tupla_atualizada[2]}")

print(f"coordenada Y = {tupla_atualizada[1]}")