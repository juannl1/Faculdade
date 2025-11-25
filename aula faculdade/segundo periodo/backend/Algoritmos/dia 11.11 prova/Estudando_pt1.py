
while True:

    numero = int(input("\nDigite um número > > > "))
    passos = 0

    if numero == 0:
        print("O número '0' Encerra o programa...")
        break
    else:
        while numero != 1:
            passos += 1
            if numero % 2 == 0:
                numero = numero // 2
                print(f"{passos}° Passo. Par: {numero}")
            else:
                numero = (numero * 3) + 1
                print(f"{passos}° Passo. Impar: {numero}")


print(f"Foram necessários {passos} para chegar no fim")