

multiplo = int(input("Digite o numero que vc deseja saber o multiplo: "))
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite o final do contador: "))

for x in range(n1, n2 + 1):
    if x % multiplo == 0:
        print(f"{x} é multplo de {multiplo}")
