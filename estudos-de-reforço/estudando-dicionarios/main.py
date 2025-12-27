import json

with open("estudos-de-reforço/estudando-dicionarios/banco-de-dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
# importando o json



input_do_usuario = "arraial_do_cabo".replace(" ", "_").lower() # Tirando os underlines do texto e trocando para o espaço " " para o if conseguir achar a cidade

print(20*"=", input_do_usuario.strip().capitalize().replace("_", " "), 20*"=", "\n")

for cidades in dados:

    if cidades == input_do_usuario:

        print(f"Estado: {dados[input_do_usuario]['estado']}\nTipo de Cidade: {dados[input_do_usuario]['tipo_de_cidade']}\nPopulação: {dados[input_do_usuario]['populacao']}")

        print("Perfil Turístico: ", end=' ')
        for i in dados[input_do_usuario]['perfil_turistico']:
            print(i, end=', ')

        print("\n")

        contagem = 1

        print("Pontos Turísticos: ")
        for i in dados[input_do_usuario]['pontos_turisticos']:
        
            print(f"{contagem}°", i)
            contagem += 1
        break
else:
    print("Cidade não encontrada...")

