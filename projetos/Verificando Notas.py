
quantidade_de_players = int(input("Qual a quantidade de players: "))

players = {}



info = []
for x in range(0, quantidade_de_players + 1):
    n1 = input("Digite o nome do player: ")
    print(f"Digite informações sobre o player {n1}")
    players['ranking'] = str(input("Ranking: "))
    players['level'] = str(input("Level: "))
    players['horas_jogadas'] = int(input("Horas Jogadas: "))
    print(f"{n1} Registrado...")
print(info)
print(f"O player {}")