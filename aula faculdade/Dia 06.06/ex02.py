#funções em python
"""
é um bloco de código reutilizável que executa uma tarefa específica.
função traz um comportamento.
"""

#lista = [1,2,3]
#lista.append(4) #função == método
#print(lista)

"""
1- organização de código
2- Reutilização de código
3- facilidade de manutenção
4- legibilidade
"""

#Prontas X cria na mão
#Criar == Declarar uma função
#def nome_da_função():
    #bloco de código

#Declaração de função - sem parâmetro

#def saudacao():
#    print("Olá, Mundo")
#saudacao()# exec função
#lista = []
#for x in range(0, 3):
#    n1 = input("Digite o nome: ")
 #   lista.append(n1)
#def boas_vindas(nome):
 #   print(f"Olá, {nome}! seja bem vindo.")
#boas_vindas(nome)

#Função com retorno (return)
#def soma (a,b):
#    return a + b
#soma(2,2)

#print(soma(2,2))
#resultado = soma(2,3)
#print(f"Resultado é = {resultado}")



#Função com parâmetros 

#def mensagem(texto = "Olá, Mundo"):
#    print(texto)

#mensagem()# Olá, mundo
#mensagem("Bom Dia !") #Bom dia !


#Escopo de variáveis
#Variável local -> escopo local == Existe apenas dentro da função
#Variável global -> escopo global == definida fora de qualquer função

def teste():
    x = 10 # local
    print(x)

x = 5 #global
teste()
print(x)
