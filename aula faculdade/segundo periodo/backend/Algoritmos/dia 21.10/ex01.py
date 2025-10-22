print("\n\n\n", 20*"-=")
print("Lista de convidados da festa de Serafim...")
print(21*"-=", "\n\n")

convidados = ["Juan", "Carlos", "Roberto", "Maria", "Joao", "Ana", "Pedro", "Juliana", "Lucas", "Mariana", "Gabriel", "Laura", "Rafael",
    "Carolina", "Matheus", "Isabela", "Felipe", "Lívia", "Guilherme", "Vitória", "Bruno", "Manuela",
    "Daniel", "Beatriz", "Eduardo", "Helena", "Gustavo", "Clara", "Ricardo", "Luiza", "Thiago",
    "Giovanna", "André", "Sofia", "Leonardo", "Alice", "Alexandre", "Valentina", "Marcelo", "Elisa",
    "Vinícius", "Larissa", "Caio", "Maitê", "Henrique", "Cecília", "Murilo", "Evelyn", "Breno",
    "Rebeca", "Arthur", "Letícia", "Hugo", "Nicole", "Miguel", "Pietro", "Brenda", "Davi",
    "Emanuelly", "Fernando", "Yasmin", "Vicente", "Esther", "Diego", "Kamilly", "Antônio",
    "Alícia", "Raul", "Stella", "Bento", "Bianca", "Benício", "Catarina", "Carlos", "Heloísa",
    "Cauã", "Lara", "Elias", "Luana", "Heitor", "Melissa", "Ian", "Lorena", "Igor", "Marina"]
contador_de_lotacao_da_festa = 0
while True:
    contador_de_lotacao_da_festa += 1
    if contador_de_lotacao_da_festa == 2:
        print("A festa já está cheia")
        break
    else:

        pesquisa = str(input("Digite o nome da pessoa: ")).capitalize()

        if pesquisa == 'sair':
                break

        else:
            if pesquisa in convidados:
                posicao_do_convidado = convidados.index(pesquisa) + 1

                print(f"O convidado {pesquisa} está na festa e foi o {posicao_do_convidado }° convidado\n")
                convidados.remove(pesquisa)

            else:
                print("Essa pessoa não está na lista de convidados ou já entrou na festa")
