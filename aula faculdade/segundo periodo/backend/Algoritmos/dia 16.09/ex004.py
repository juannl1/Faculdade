#pedra, papel, tesoura

player1 = str(input("Digite sua opção: ")).lower().strip()
player2 = str(input("Digite sua opção: ")).lower().strip()


if player1 == 'pedra' and player2 == 'tesoura': #pedra ganha
    print("Player 1 ganhou, Pedra")

elif player1 == 'pedra' and player2 == 'papel':
    print("Player 2 ganhou, Papel")

elif player1 == 'tesoura' and player2 == 'papel':
    print("Player 1 ganhou, Tesoura")

elif player1 == 'tesoura' and player2 == 'pedra':
    print("Player 2 ganhou, Pedra")

elif player1 == 'papel' and player2 == 'pedra':
    print("Player 2 ganhou, Pedra")

elif player1 == 'papel' and player2 == 'tesoura':
    print("Player 1 ganhou, Papel")

else:
    print("Empate")