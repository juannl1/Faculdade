#Juan Dos Anjos Lemos
#202515173

numero1 = int(input("Digite um número: "))
numero_para_divisao = int(input("Digite um divisor: "))

multiplo = numero1 % numero_para_divisao

if multiplo == 0:
    print(f"É multiplo de {numero_para_divisao}")
else:
    print(f"Não é multiplo de {numero_para_divisao}")

if numero1 > 0:
    print(f"O número {numero1} é positivo")
elif numero1 < 0:
      print(f"O número {numero1} é negativo")
else:
    print(f"O número é 0")