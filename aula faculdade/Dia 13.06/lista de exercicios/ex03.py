"""
🔹 3️⃣ Conjuntos
Crie dois conjuntos de nomes (com pelo menos 3 nomes cada), digitados pelo usuário. Depois:

Mostre os nomes que aparecem nos dois conjuntos.

Mostre os nomes que aparecem em pelo menos um dos conjuntos (união).
"""

nome1 = str(input("Nome 1: "))
nome2 = str(input("Nome 2: "))
nome3 = str(input("Nome 3: "))

print("\nConjunto 2\n")

nome4 = str(input("Nome 1: "))
nome5 = str(input("Nome 2: "))
nome6  = str(input("Nome 3: "))

conjunto1 = {nome1, nome2, nome3}
conjunto2 = {nome4, nome5, nome6}
print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

intersecao = conjunto1.intersection(conjunto2)

uniao = conjunto1.union(conjunto2)
if intersecao == set():
    print("Não tem nomes iguais, sem interseção")

else:
    print(f"Nomes que aparecem no mesmo conjunto: {intersecao}")
print(f"A união dos 2 conjunto de nomes são : {uniao}")