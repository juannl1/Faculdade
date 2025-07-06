"""
🟢 2️⃣ Tuplas — Acesso por índice
Crie uma tupla com quatro nomes digitados pelo usuário. Depois:

Mostre o primeiro e o último nome.

Verifique se o nome "Maria" está na tupla.

Exiba todos os nomes, um por linha.
"""

n1 = str(input("Digite um nome: ")).strip().lower()
n2 = str(input("Digite um nome: ")).strip().lower()
n3 = str(input("Digite um nome: ")).strip().lower()
n4 = str(input("Digite um nome: ")).strip().lower()

tupla = (n1, n2, n3, n4)

if 'maria' in tupla:
    print("\nMaria está na tupla\n")
else:
    print("\nMaria não está na tupla\n")

for x, nomes in enumerate(tupla, start=1):
    print(f"{x}° nome: {nomes}")
