class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        lista_planos = ["basic", "premium"]
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido") # raise = provocar erro e Exception = ("mnotivo do erro")
        self.plano = plano

cliente = Cliente("Juan", "jlemos329@gmail.com", "dasdwa")
