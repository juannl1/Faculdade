class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas
    
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "bateu a meta...")
        else:
            print(self.nome, " Não bateu a meta...")



vendedor1 = Vendedor("Juan Lemos")
vendedor1.vendeu(1400)
vendedor1.bateu_meta(500)

vendedor2 = Vendedor("Elon Musk")
vendedor2.vendeu(400)
vendedor2.bateu_meta(500)


