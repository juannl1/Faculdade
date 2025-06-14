import time, random
randomizar = random.randint(0, 10)




def andar_carro():
    print("Aperte ENTER para andar com o carro")
    time.sleep(1)
    for c in range(0, randomizar + 1):
        
        print(f"Você andou {c} vezes.\n")
        input(("Ande com o carro... "))
    print("Você chegou em um semáforo.\n")
def sinal():
    print("Você está passando por um semáforo...")
    n1 = str(input("Qual a cor do sinal ? (🟢 Verde, 🟡 Amarelo ou 🔴 Vermelho):")).strip().lower()
    
    if n1 == "verde":
        print("🟢 Verde, siga em frente...")
    elif n1 == "amarelo":
        print("🟡 Amarelo, Atenção... ")
    elif n1 == "vermelho":
        print("🔴 Vermelho, Pare !!!")
    else:
        print("O sinal está com problema. Tente novamente.")
    return(n1)
andar_carro()
sinal()




resultado_sinal = sinal()


if resultado_sinal == "verde":
    print("Agora q vc avançou o semáforo... Continue")
elif resultado_sinal == "vermelho":
    print("V")