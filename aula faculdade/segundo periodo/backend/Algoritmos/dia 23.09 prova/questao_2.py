 #nome: Juan Dos Anjos lemos
#matricula: 202515173



nota_teste_1 = float(input("Digite a nota do teste 1: "))
nota_prova_1 = float(input("Digite a nota da prova 1: "))
nota_teste_2 = float(input("\nDigite a nota do teste 2: "))
nota_prova_2 = float(input("Digite a nota da prova 2: "))
 
teste = (nota_teste_1 + nota_teste_2) * 2
prova = (nota_prova_1 + nota_prova_2) * 8
media = (teste + prova) / 20



print(f"Sua média é {media}")

if media >= 7.0:
    print("Situação: Aprovado")

elif media >= 4.0 and media < 6.9:
    print("Situação: Prova final")

else:
    print("Situação: Reprovado")

