import random, time

lista_de_bets = [
    #Futebol
    "Sobre Futebol...\n\nO jogador chutou a bola. \n\nFoi gol ou não?",
    "Sobre Futebol...\n\nO goleiro pulou para o lado certo. \n\nDefendeu ou não?",
    "Sobre Futebol...\n\nO árbitro consultou o VAR. \n\nMarcou pênalti ou não?",
    "Sobre Futebol...\n\nO atacante estava impedido. \n\nO gol foi anulado ou não?",
    "Sobre Futebol...\n\nO zagueiro tocou com a mão na bola. \n\nO juiz marcou pênalti ou não?",
    "Sobre Futebol...\n\nO técnico fez uma substituição ofensiva. \n\nO time marcou um gol depois ou não?",
    "Sobre Futebol...\n\nO jogador recebeu um cartão amarelo. \n\nFoi expulso depois ou não?",
    "Sobre Futebol...\n\nO time ganhou o escanteio. \n\nConverteu em gol ou não?",
    "Sobre Futebol...\n\nO atacante ficou cara a cara com o goleiro. \n\nFez o gol ou não?",
    "Sobre Futebol...\n\nO jogador cobrou a falta direta. \n\nAcertou o gol ou não?",
    "Sobre Futebol...\n\nO time perdeu um jogador por lesão. \n\nGanhou o jogo mesmo assim ou não?",
    "Sobre Futebol...\n\nO juiz deu mais de 5 minutos de acréscimo. \n\nSaiu gol nos acréscimos ou não?",
    "Sobre Futebol...\n\nO lateral bateu um arremesso rápido. \n\nCriou uma jogada perigosa ou não?",
    "Sobre Futebol...\n\nO jogador fez embaixadinhas no jogo. \n\nFoi advertido pelo árbitro ou não?",
    "Sobre Futebol...\n\nO time teve mais posse de bola. \n\nVenceu a partida ou não?",
    "Sobre Futebol...\n\nO jogador chutou a bola. \n\nFoi gol ou não?",
    "Sobre Futebol...\n\nO goleiro pulou para o lado certo. \n\nDefendeu ou não?",
    "Sobre Futebol...\n\nO árbitro consultou o VAR. \n\nMarcou pênalti ou não?",
    "Sobre Futebol...\n\nO atacante estava impedido. \n\nO gol foi anulado ou não?",
    "Sobre Futebol...\n\nO zagueiro tocou com a mão na bola. \n\nO juiz marcou pênalti ou não?",
    "Sobre Futebol...\n\nO técnico fez uma substituição ofensiva. \n\nO time marcou um gol depois ou não?",
    "Sobre Futebol...\n\nO jogador recebeu um cartão amarelo. \n\nFoi expulso depois ou não?",
    "Sobre Futebol...\n\nO time ganhou o escanteio. \n\nConverteu em gol ou não?",
    "Sobre Futebol...\n\nO atacante ficou cara a cara com o goleiro. \n\nFez o gol ou não?",
    "Sobre Futebol...\n\nO juiz deu mais de 5 minutos de acréscimo. \n\nSaiu gol nos acréscimos ou não?",

    #Futsal
    "Sobre Futsal...\n\nO goleiro-linha entrou em quadra. \n\nO \n\ntime empatou o jogo ou não?",
    "Sobre Futsal...\n\nO jogador bateu lateral com pressa. \n\nCriou chance clara de gol ou não?",
    "Sobre Futsal...\n\nA equipe cometeu 5 faltas no tempo. \n\nSofreu tiro livre direto ou não?",
    "Sobre Futsal...\n\nO pivô recebeu de costas para o gol. \n\nFinalizou com perigo ou não?",
    "Sobre Futsal...\n\nO jogador fez um drible no um contra um. \n\nGanhou o duelo ou não?",

    # Vôlei
    "Sobre Volei...\n\nO time sacou com força. \n\nConseguiu ace ou não?",
    "Sobre Volei...\n\nA equipe pediu desafio. \n\nA bola foi dentro ou não?",
    "Sobre Volei...\n\nO atacante explorou o bloqueio. \n\nA bola tocou no adversário ou não?",
    "Sobre Volei...\n\nO time salvou uma bola difícil na defesa. \n\nGanhou o ponto depois ou não?",
    "Sobre Volei...\n\nO bloqueio foi montado com dois jogadores. \n\nPararam o ataque ou não?",

    # Surf
    "Sobre Surf...\n\n*O surfista entrou na onda. \n\nCompletou a manobra ou não?",
    "Sobre Surf...\n\n*O atleta pegou uma onda grande. \n\nGanhou nota acima de 8.0 ou não?",
    "Sobre Surf...\n\n*O surfista caiu durante a manobra. \n\nConseguiu se recuperar ou não?",
    "Sobre Surf...\n\n*O competidor esperou por uma série de ondas a bateria toda. \n\nPegou a melhor onda da bateria ou não?",
    "Sobre Surf...\n\n*O surfista tentou um aéreo. \n\nConseguiu completar a manobra ou não?"
]
lista_de_odds = {

    0: ['Sim',2.38, 'Não', 2.26],
    1: ['Sim', 2.33, 'Não', 2.22],
    2: ['Sim', 2.10, 'Não', 1.96],
    3: ['Sim', 1.86, 'Não', 1.80],
    4: ['Sim', 2.11, 'Não', 1.85],
    5: ['Sim', 2.46, 'Não', 2.05],
    6: ['Sim', 4.45, 'Não', 1.15],
    7: ['Sim', 6.56, 'Não', 1.25],
    8: ['Sim', 2.49, 'Não', 2.17],
    9: ['Sim', 6.99, 'Não', 1.12],
    10: ['Sim', 2.16, 'Não', 2.17],
    11: ['Sim', 2.38, 'Não', 1.73],
    12: ['Sim', 2.00, 'Não', 1.63],
    13: ['Sim', 4.12, 'Não', 1.12],
    14: ['Sim', 2.10, 'Não', 2.05],
    15: ['Sim', 2.43, 'Não', 2.06],
    16: ['Sim', 2.19, 'Não', 2.04],
    17: ['Sim', 2.43, 'Não', 1.79],
    18: ['Sim', 2.10, 'Não', 1.97],
    19: ['Sim', 2.01, 'Não', 1.78],
    20: ['Sim', 2.26, 'Não', 2.05],
    21: ['Sim', 4.53, 'Não', 1.11],
    22: ['Sim', 7.04, 'Não', 1.30],
    23: ['Sim', 2.02, 'Não', 2.14],
    24: ['Sim', 2.13, 'Não', 1.78],
    25: ['Sim', 2.20, 'Não', 2.09],
    26: ['Sim', 2.18, 'Não', 2.16],
    27: ['Sim', 1.84, 'Não', 1.78],
    28: ['Sim', 1.92, 'Não', 1.79],
    29: ['Sim', 1.93, 'Não', 1.63],
    30: ['Sim', 1.94, 'Não', 1.77],
    31: ['Sim', 2.18, 'Não', 2.00],
    32: ['Sim', 2.10, 'Não', 1.96],
    33: ['Sim', 1.83, 'Não', 1.69],
    34: ['Sim', 2.17, 'Não', 2.07],
    35: ['Sim', 2.14, 'Não', 2.00],
    36: ['Sim', 2.35, 'Não', 2.07],
    37: ['Sim', 2.95, 'Não', 1.65],
    38: ['Sim', 2.38, 'Não', 1.65],
    39: ['Sim', 2.91, 'Não', 1.75],
    40: ['Sim', 2.60, 'Não', 1.65],
    41: ['Sim', 2.53, 'Não', 1.72]
}

bet_sorteada = random.choice(lista_de_bets)
posição_bet_sorteada = lista_de_bets.index(bet_sorteada)
lista_sim_ou_nao = ["Sim", "Não"]
sim_ou_nao = random.choice(lista_sim_ou_nao)


def funcionamento_da_casa_de_apostas():
    print(bet_sorteada)
    print(f"\nOdds:\n\nSim: ODD: {lista_de_odds[posição_bet_sorteada][1]}\nNão: ODD: {lista_de_odds[posição_bet_sorteada][3]}")

    decisao = int(input("1. Sim\n2. Não\n= "))
    while True:
        if decisao == 1 or decisao == 2:
            break
        else:
            print("\nTente novamente...\n\n")
            time.sleep(1)
            decisao = int(input("1. Sim\n2. Não\n= "))

            
        
        
    aposta = float(input("\nValor da aposta: "))
    odd = lista_de_odds[posição_bet_sorteada][1]
    

    resposta = sim_ou_nao
    if resposta == "Sim" and decisao == 1:
        for x in range(1, 4):
            print(f"{x}")
            time.sleep(0.5)
        print("Você ganhou")
        recompensa = aposta * lista_de_odds[posição_bet_sorteada][1]
        time.sleep(1.5)
        print(f"Seu saldo: {recompensa}")

    elif resposta == "Sim" and decisao == 2:
        print("Você perdeu")

    elif resposta == "Não" and decisao == 2:
        for x in range(1, 4):
            print(f"{x}")
            time.sleep(0.5)
        print("Você ganhou")
        recompensa = aposta * lista_de_odds[posição_bet_sorteada][3]
        print(f"Seu saldo: {recompensa}")

    elif resposta == "Não" and decisao == 1:
        print("Você perdeu")

    else:
        print("Decisão inválida")
    







"""#Início
print(20*"=","APOSTE JÁ", 20*"=")

print("\n\nBem vindo a APOSTE JÁ, a casa de aposta que te da 50% de vencer\n")
print("Vamos Começar...\n\n")"""

funcionamento_da_casa_de_apostas()