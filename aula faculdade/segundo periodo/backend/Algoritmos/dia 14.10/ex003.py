
import random, time

def joguinho():
    sorteando = random.randint(1, 10)
    print(sorteando)
    while True:
        numero_escolhido = int(input("Qual o seu palpite? > > > "))

        if numero_escolhido < sorteando:
            print("Escolha um número maior...\n")
        elif numero_escolhido > sorteando:
            print("Escolha um número menor...\n")
        else:
            print("Ganhou !!!")

            opcao = str(input("Deseja jogar de novo?\n> > > "))

            if opcao == 'sim':
                print("Ok, vamos lá")
                joguinho()
            else:
                break
joguinho()

