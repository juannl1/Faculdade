"""
🔹 2️⃣ Tuplas
Crie uma Tupla com três coordenadas (x, y, z) informadas pelo usuário. Depois:

Exiba as coordenadas separadamente (uma por linha).

Mostre o valor da coordenada y.
"""

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = int(input("Digite o valor de Z: "))
coordenadas = (x, y , z)
for x, valor in enumerate(coordenadas, start=1):
    print(f"{x}° coordenada: {valor}")