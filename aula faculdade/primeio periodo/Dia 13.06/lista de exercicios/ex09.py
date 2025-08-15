"""
🔹 9️⃣ Função com conjunto
Crie uma função disciplinas_comuns(d1, d2) que receba dois conjuntos de disciplinas e retorne o conjunto com as disciplinas em comum. Mostre o resultado no programa principal.
"""

disciplina_aluno1 = {"História", "Química", "Filosofia", "Sociologia", "Ciência da Computação", "Astronomia", "Ciências" "Políticas", "Artes"}
disciplina_aluno2 = {"Matemática", "Geografia", "Química", "Filosofia", "Ciência da Computação", "Sociologia", "Astronomia"}
def disciplinas_comuns(d1, d2):
    intercesecao = d1.intersection(d2)
    print(f"A interseção dos conjuntos é: {intercesecao}")
disciplinas_comuns(disciplina_aluno1, disciplina_aluno2)
