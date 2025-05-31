alunos = ["Ana", "João", "Juan"]
#Dicionario notas

notas_alunos = {}

for aluno in alunos:
    print(f"\n Digite as notas para {aluno}: ")
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Nota{i}: "))
        notas.append(nota)
    notas_alunos[aluno] = notas
print("\n-- Boletim Final--")
for aluno, nota in notas_alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno}: Notas = {nota}")