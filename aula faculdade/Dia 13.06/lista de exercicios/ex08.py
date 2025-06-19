"""
🔹 8️⃣ Função com retorno
Crie uma função media3(n1, n2, n3) que calcule e retorne a média de três notas. O programa deve exibir se o aluno está aprovado (média ≥ 7) ou reprovado.
"""

def media3(n1, n2, n3):
    media = (n1 + n2 + n3) / 2

    if media >= 7:
        print(f"Sua média foi {media}. Aprovado.")

    else: 
        print(f"Sua média foi {media}. Reprovado.")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
print("Você precisa de 7 ou mais para ser Aprovado")
media3(n1, n2, n3)