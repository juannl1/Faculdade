#dicionário: Estrutura de daos que armazenam informações em pares chamados "CHAVE/VALOR"
#aluno1 = {
#   "nome":"Juan",
 #   "idade": 18,
  #  "curso": "ADS"
#}
#aluno2 = {
 #   "nome": "Pedro",
#    "idade": "18",
 #   "sexualidade": "afeminado"
#}
#aluno1_nome = "Pedro"
#aluno1_idade = "18"
#aluno1_genero = "Feminino"
#print(f"O nome do aluno é {aluno1_nome} idade {aluno1_idade} genero {aluno1_genero}")
#print(f"O {aluno1['nome']} tem {aluno1['idade']} e é {aluno1['sexualidade']}")

aluno = {
    "nome": "Joao",
    "idade": 21,
    "curso": "Engenharia de software" 
}
aluno["idade"] = 49 #modificando chave
aluno["email"] = "jlemos329@gmail.com" #add chave 
#print(aluno['email'])
#del aluno["curso"]
#valor = aluno.pop("curso")


if "curso" in aluno:
    print(f"Curso está presente e é {aluno['curso']}")
else:
    print("Curso n está presente")