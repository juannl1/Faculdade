t1 = float(input("Digite a nota do trabalho 1: "))
t2 = float(input("Digite a nota do trabalho 2: "))
p1 = float(input("Digite a nota da prova 1: "))
p2 = float(input("Digite a nota da prova 2: "))


nota1 = t1*0.2 + p1*0.8
nota2 = t2*0.2 + p2*0.8

media = (nota1 + nota2) / 2

print(f"Sua média é: {media}")