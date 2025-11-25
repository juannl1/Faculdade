#Juan Dos Anjos lemos
#202515173  

print("Calculo de área\n")

opcoes = str(input("Você quer calcular qual ?\nQuadrado\nTriângulo\nCírculo\n\n > > > ")).strip().lower()

if opcoes == 'quadrado':
    lado = float(input("Digite o lado do quadrado: "))
    area_do_quadrado = lado * lado
    print(f"A área do quadrado é: {area_do_quadrado}")

elif opcoes == 'triangulo' or opcoes == 'triângulo':
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))

    area_do_triangulo = (base * altura) / 2
    print(f"A área do Triângulo é {area_do_triangulo}")

elif opcoes == 'circulo' or opcoes == 'círculo':
    raio = float(input("Digite o raio do círculo: "))

    area_do_circulo = 3.14 * (raio ** 2)
    print(f"A area do círculo é: {area_do_circulo}")

else:
    print("Entrada Inválida.\n\nTente Novamente...")



