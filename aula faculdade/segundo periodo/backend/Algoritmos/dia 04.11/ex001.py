


print("Login\n\n")

#senha = str(input("SENHA > "))
senha = 'senha123'

tamanho = False
maiusculo = False
minusculo = False
digitos = False
caracter_especial = False


if len(senha) <= 8:
    tamanho = True

for letra in senha:
    if letra.isupper():
        maiusculo = True
    if letra.islower():
        minusculo = True
    if letra.isdigit():
        digitos = True
    if letra in ["!", "@", "#", "$", "%", "&", "*", "?", "_"]:
        caracter_especial = True
if tamanho and maiusculo and minusculo and digitos and caracter_especial:
    print("SUCESSO")

if tamanho == False:
    print("Não tem o tamanho minimo")
if maiusculo == False:
    print("NÃO TEM MAIUSCULA")
if minusculo == False:
    print("não tem minuscula")
if digitos == False:
    print("Não tem numeros")

