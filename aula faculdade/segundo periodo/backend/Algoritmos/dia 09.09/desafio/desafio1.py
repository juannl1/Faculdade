idade = int(input("Digite a idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
else:
    if idade >= 13 and idade <= 17:
        print("Adolescente")
    else:    
        if idade >= 18 and idade <= 64:
            print("Adulto")
        else:
            print("idoso")
        
    