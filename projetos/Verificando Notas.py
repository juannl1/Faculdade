print("Cadastrando rankings de jogadores\n")



quantidade_players = int(input("Digite a quantidade de players: "))


nickname = [ ]
players = { }
for i in range(1, quantidade_players + 1):
    players["player"] = str(input(f"{i}° Nickname: "))
    players["ranking"] = str(input("Ranking: "))
    players["Level"] = int(input("Level: "))
    nickname.append(players["player"])
