
numero_de_alunos = int(input("Digite a qtd de alunos: "))

lista_das_medias = []
aluno = 0
for x in range(1, numero_de_alunos + 1):
    aluno += 1

    print(aluno, "° Aluno")
    nota_teste = float(input("Digite a nota: "))
    nota_prova = float(input("Digite a nota: "))
    print("próximo\n")
    
    media = (nota_prova + nota_teste) / 2
    lista_das_medias.append(media)
    
for i, x in enumerate(lista_das_medias, start= 1):
    print(f"{i}° Aluno: nota: {x:.2f}")
    
    if x <= 7:
        situacao = print("Reprovado...")
    else:
        situacao = print("Aprovado")
