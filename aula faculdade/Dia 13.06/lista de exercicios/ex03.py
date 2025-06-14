"""
🔹 3️⃣ Conjuntos
Crie dois conjuntos de nomes (com pelo menos 3 nomes cada), digitados pelo usuário. Depois:

Mostre os nomes que aparecem nos dois conjuntos.

Mostre os nomes que aparecem em pelo menos um dos conjuntos (união).
"""
lista1 = []
lista2 = []
for c in range(1, 4):
    n1 = str(input(f"Digite o {c}° nome para o primeiro conjunto: "))
    lista1.append(n1)
print("\nSegundo Conjunto...\n")
for c in range(1, 4):
    n2 = str(input(f"Digite o {c}° nome para o segundo conjunto: "))
    lista2.append(n2)
conjunto1 = set(lista1)
conjunto2 = set(lista2)
print(f"O primeiro conjunto é: {conjunto1}\nO segundo conjunto é: {conjunto2}")
uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
print(f"\nUnião: {uniao}\n")
print(f"Interseção: {intersecao}\n")