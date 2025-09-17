n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 2° número: "))

if n1 > n2 and n1 > n3: #n1 maior de todos
    print("O núrmero maior é o ", n1)
else:
    if n2 > n1 and n2 > n3: #n2 maior de todos
        print("O núrmero maior é o ", n2)
    else:
        print("O núrmero maior é o ", n3)
