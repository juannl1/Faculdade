#nome: Juan Dos Anjos lemos
#matricula: 202515173



peso_do_usuario = float(input("Digite o seu peso > > > "))
altura_do_usuario = float(input("Digite sua altura > > > "))

calculo_imc = (peso_do_usuario/altura_do_usuario) / altura_do_usuario

print(f"\nO seu IMC (ÍNDICE DE MASSA CORPORAL) é {calculo_imc:.2f}")

if calculo_imc < 18.5: #abaixo do peso
    print("Classificação: Abaixo do peso...")

elif calculo_imc >= 18.5 and calculo_imc < 24.9: #Peso normal
    print("\nClassificação: Peso normal...")

elif calculo_imc >= 24.9 and calculo_imc < 29.9: #Sobrepeso
    print("\nClassificação: Sobrebeso...")

else: # >= 29.90
    print("\nClassificação: Obesidade")


    
