"""crie um programa que peça ao usuario para digitar sua idade em anos. Em seguida, o programa deve calcular a idade do usuario em meses e dias"""

idade = int(input("Digite sua idade: "))

idade_em_dias = idade * 365
idade_em_meses = idade * 12

print(f"\nVocê viveu por: {idade_em_dias} dias\nVocê viveu por: {idade_em_meses} meses")

