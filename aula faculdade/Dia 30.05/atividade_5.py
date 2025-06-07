estudantes = {}

quantidade_estudantes = int(input("Quantidade de estudantes: "))

for i in range(1, quantidade_estudantes + 1):
    nome = input(f"Digite o nome do estudante {i}: ")
    notas = []
    for j in range(1, 4):
        nota = float(input(f"Digite a nota: {j} de {nome}: "))
        notas.append(nota)
    estudantes[nome] = notas
print(estudantes)
print("\n --Resultado Final--")
for nome, notas in estudantes.items():
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    print(f"{nome}: Notas = {notas}, Média = {media:.2f} => {status}")