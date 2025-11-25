

numero_escolhido = int(input("Digite um número > > > "))

def identificar_numero_primo(numero_para_calcular):

    lista_de_numeros_primos = []

    for num in range(2, numero_para_calcular + 1):
        contador_de_divisores = 0

        for i in range(1, num + 1):

            if num % i == 0:
                contador_de_divisores += 1
            else:
                pass

        if contador_de_divisores == 2:
            lista_de_numeros_primos.append(num)

    return lista_de_numeros_primos

lista = identificar_numero_primo(numero_escolhido)

print(lista)
