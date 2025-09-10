"""comprovante = input("Deseja imprimir o comprovante: ")

if comprovante == "sim":
    print("Imprimindo comprovante")
    
print("Finalizando")


numero = (input("> > > "))

if numero % 2 == 0:
    print("Par\n")
else:
    print("Impar\n")"""

n1 = float(input("Digite o 1° float > > > "))
n2 = float(input("Digite o 2° float > > > "))

if n1 < n2:
    print("o menor número é: ", n1)

else:
    if n1 == n2:
        print("São iguais...")

    else:
        if n1 > n2:
            print("o menor numero é: ", n2)