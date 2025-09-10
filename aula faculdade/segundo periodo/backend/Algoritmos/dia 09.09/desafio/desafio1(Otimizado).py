idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")
else:
    if idade <= 17:
        print("Adolescente")
    else:    
        if idade <= 64:
            print("Adulto")
        else:
            print("idoso")