"""
🔵 3️⃣ Conjuntos — Operações de conjunto
Solicite dois conjuntos de cores preferidas de duas pessoas diferentes. Depois:

Mostre as cores em comum.

Mostre as cores que só a primeira pessoa gosta.

Verifique se os conjuntos são disjuntos (sem elementos em comum).
"""

print("1° Pessoa.\n")
cores1 = str(input("Digite suas cores favoritas separadas por espaços: "))

print("2° Pessoa.")
cores2 = str(input("Digite suas cores favoritas separadas por espaços: "))

cor1 = set(cores1.split()) #conjunto 1
cor2 = set(cores2.split()) #conjunto 2


print("\n1° pessoa\n")

for x, cores in enumerate(cor1, start=1):
    print(f"{x}° Cor:", *cores)

print("\n2° pessoa\n")

for x, cores in enumerate(cor2, start=1):
    print(f"{x}° Cor:", *cores)

print(f"\n1° pessoa gosta das cores:", *cor1)
print(f"\n2° pessoa gosta das cores:", *cor2)

intersecao = cor1.intersection(cor2)

if intersecao == set():
    print("\nSem cores em comum...")
else:
    print("\nVocês gostam das mesmas cores:", *intersecao)