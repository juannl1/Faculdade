a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b ** 2) - 4 * a * c

posicao_x = -b/(2 * a)
posicao_y = -delta / (4 * a)


print("a = 1\nb = -5\nc = 6")

print(f"\nO delta é {delta}\n\nVértice X = {posicao_x:.2f}\nVértice Y = {posicao_y:.2f}")