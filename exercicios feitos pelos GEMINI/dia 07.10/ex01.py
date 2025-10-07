"""Criando programa de números primos"""


n1 = int(input("Digite um número > > > "))
n2 = int(input("Até que numero vc deseja > > > "))

for x, indice in range(n1, n2 + 1, start=1):
    calculo_numero_primo = n1 / indice

    if calculo_numero_primo == 1:
        print(n2)