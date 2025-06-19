import time, math
print("Calculadora Interativa\n\n")

inicio = str(input("Digite se você quer uma Tabuada ou Cálculo específico\nDigite 'tabuada' ou 'calculo' > ")).lower().strip()

if inicio == 'tabuada':
    print("Qual operador você dejesa usar?\n\nX = Multiplicação\n+ = Soma\n- = ")
