
def contar_passos_collatz(indice):

    passos = 0

    while indice != 1:

        if indice % 2 == 0:
            indice = indice // 2

        else:
            indice = (3 * indice) + 1

        passos += 1

    return passos

def Mapeamento_collatz(numero):
    resultado = {}

    for num in range(2, numero + 1):

        passos = contar_passos_collatz(num)

        resultado[str(num)] = passos

    return resultado

numero_escolhido = int(input("Digite outro numero: "))

resultado = Mapeamento_collatz(numero_escolhido)
print(resultado)
