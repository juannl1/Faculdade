"""
🔹 7️⃣ Função com parâmetro
Crie uma função tabuada(numero) que exiba a tabuada de multiplicação de 1 a 10 do número informado.
"""

def tabuada(numero):
    for c in range(1, 11):
        total = numero * c
        print(f"{numero} x {c} = {total}")

        
n1 = int(input("Digite o número que você deseja tabuar: "))
tabuada(n1)