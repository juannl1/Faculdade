cadastros = []
for i in range(0, 3):
    aluno = {}
    aluno["nome"] = input("\nNome: ")
    aluno["idade"] = input("Idade: ")
    aluno["curso:"] = input("Curso: ")
    cadastros.append(aluno)
    print("\nCadastrado.")
for a in cadastros:
    print(a)