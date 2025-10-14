


opcao = str(input("Escolha uma operação: \n1. -\n2. +\n3. *\n4. /\n> > > "))

while (opcao == '-') or (opcao == '+') or (opcao == '*') or (opcao == '/'):

    n1 = float(input("Digite um valor: "))
    n2 = float(input("Digite um valor: "))

    if opcao == '-':
        print(n1 - n2)
    
    elif opcao == '+':
        print(n1 + n2)
    
    elif opcao == '*':
        print(n1 * n2)
    
    else:
        print(n1 / n2)

print("fim...")