n1 = int(input("Digite > > > "))

if n1 % 2 == 0:
    print("Par...")
    if n1 >= 100:
        print(n1, "Maior que 100")
    else:
        print(n1, "Menor que 100")

else:
    print("Impar...")
    if n1 <= 100:
        print(n1, "Menor que 100")
    else:
        print(n1, "Maior que 100")
    