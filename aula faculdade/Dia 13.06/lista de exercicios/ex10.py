"""
🔹 🔟 Escopo de variáveis
Crie um programa que tenha uma variável global x = 10. Faça uma função mostra_local() que crie uma variável x = 20 local e exiba o valor. Depois, fora da função, exiba novamente o valor de x.

"""

global x
x = 10
def mostrar_local():
    x = 20
    print(x)
mostrar_local()
print(x)
