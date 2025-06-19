"""
✅ Desafio bônus
Monte um pequeno cadastro de alunos com:

Nome

Idade

Curso

Disciplinas (conjunto)

Cadastre 2 alunos e exiba:

Os dados de cada um.

As disciplinas em comum.
"""

print("Cadastro de alunos")

qtd_alunos = int(input("Quantidade de alunos para cadastrar: "))

cadastros_aluno = []
for c in range(1, qtd_alunos + 1):
    disciplinas = {}
    disciplinasLista = list(disciplinas)
    alunos = {}
    alunos["nome"] = str(input("Nome: "))
    alunos["idade"] = int(input("Idade: "))
    alunos["curso"] = str(input("Curso: "))
    disciplinas["disciplina"] = str(input("Disciplina: "))
    c + 1
    print(f"\n{c}° Aluno cadastrado.\n")
    cadastros_aluno.append(alunos)
    disciplinasLista.append(disciplinas)
print(cadastros_aluno)
print(disciplinas)




#incompleto