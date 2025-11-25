#Juan Dos Anjos Lemos
#202515173

def Conjectura_de_Collatz(numero):

    passos = 0

    numeros_de_collatz = []
    while numero != 1:

        passos += 1

        if numero % 2 == 0:
            numero = numero // 2
            
            numeros_de_collatz.append(numero)
        else:
            numero = (numero * 3) + 1
            
            
            numeros_de_collatz.append(numero)
        
    for x in numeros_de_collatz:
        print(x, end=' -> ')
    print(f"\n\nForam necessários {passos} para chegar até 1")



numero_parametro = int(input("Digite um numero: "))
Conjectura_de_Collatz(numero_parametro)

