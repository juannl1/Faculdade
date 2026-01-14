from datetime import datetime, timedelta



class FormularioOnibus():
    def __init__(self, matricula, ponto_de_controle, dia, numero_da_linha, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local):
        
        self.matricula = matricula # poderia ter uma verificação em um possivel banco de dados
        self.ponto_de_controle = ponto_de_controle
        self.dia = dia # contém verificação
        self.numero_da_linha = numero_da_linha
        self.numero_do_carro = numero_do_carro
        self.matricula_do_motorista = matricula_do_motorista # poderia ter uma verificação em um possivel banco de dados
        self.hora_de_saida = hora_de_saida 
        self.hora_de_chegada = hora_de_chegada
        self.roleta_inicial = roleta_inicial
        self.roleta_local = roleta_local

        pontos_de_contole = ["ESTAÇÃO N.S. MERCÊS (RIO)", "ESTAÇÃO JOÃO BRASIL (NIT)", "ESTAÇÃO N.S. MERCÊS (VOLTA)", "ESTAÇÃO JOÃO BRASIL (VOLTA)", "TRIBOBÓ VOLTA (RIO)", "TRIBOBÓ VOLTA (NIT)", "TRIBOBÓ URB"]

        linhas = []
# Métodos

    # Verificar se há pessoas em pé no carro

    def verificar_lotacao(self, roleta_inicial, roleta_local):
        calculo_de_pessoas_no_onibus = roleta_inicial - roleta_local
        calculo_de_pessoas_em_pe = 52 - calculo_de_pessoas_no_onibus

        if calculo_de_pessoas_no_onibus > 52:
            print(f"O ônibus está lotado {calculo_de_pessoas_no_onibus}/52\n{calculo_de_pessoas_em_pe} pessoas em pé")
        
        elif calculo_de_pessoas_no_onibus < 52:
            print(f"O Ônibus com vaga {calculo_de_pessoas_no_onibus}/52")
    

    # Verificando se o a data está entre 1 a 31
    def verificar_data_correta(self, dia):
        if dia <= 1 and dia >= 31:
            self.dia = dia
        else:
            raise ValueError # Caindo no erro de valor para o programa perguntar de novo o dia correto
        
    
    # Verificando quanto tempo demorou para chegar no destino
    def tratar_horario(self, hora):
        # Remove ":" ou espaços que o usuário possa digitar
        limpo = hora.replace(":", "").strip()
        
        # Se o usuário digitou algo como "730", vira "0730"
        if len(limpo) == 3:
            limpo = "0" + limpo
        
        # Converte para objeto de tempo (HHmm)
        return datetime.strptime(limpo, "%H%M")

    #def salvando_itens():


# INICIANDO FORMULÁRIO

while True:
    try:
        matricula_do_fiscal = int(input("Número da matrícula: "))
        break
    except ValueError:
        print("Tente novamente...\n")

while True:
    try:
        ponto_de_controle = int(input("1.ESTAÇÃO N.S. MERCÊS (RIO)\n2.ESTAÇÃO JOÃO BRASIL (NIT)\n3.ESTAÇÃO N.S. MERCÊS (VOLTA)\n4.ESTAÇÃO JOÃO BRASIL (VOLTA)\n5.TRIBOBÓ VOLTA (RIO)\n6.TRIBOBÓ VOLTA (NIT)\n"))

        if ponto_de_controle in [1 ,2 ,3 ,4 ,5 ,6]:
            break
        else:
            
            ValueError

    except ValueError:
        



"""while True:

    try:
        matricula_do_fiscal = int(input("Número da matrícula: "))

    except:
        print("Tente novamente...")

    try:
        ponto_de_controle = int(input("1.ESTAÇÃO N.S. MERCÊS (RIO)\n2.ESTAÇÃO JOÃO BRASIL (NIT)\n3.ESTAÇÃO N.S. MERCÊS (VOLTA)\n4.ESTAÇÃO JOÃO BRASIL (VOLTA)\n5.TRIBOBÓ VOLTA (RIO)\n6.TRIBOBÓ VOLTA (NIT)\n"))

        if ponto_de_controle not in [1,2,3,4,5,6]:
            raise ValueError
        
    except ValueError:
        print("Tente novamente...")
        raise ValueError

    try:
        dia_de_hoje = int(input("Dia de hoje: "))
        FormularioOnibus.verificar_data_correta(dia_de_hoje)

    except ValueError:
        print("Tente novamente...")
        raise ValueError

    try:
        numero_do_carro = int(input("Número do carro: "))

    except ValueError:
        print("Tente novamente...")
        raise ValueError

    try:
        matricula_do_motorista = int(input("Matrícula do motorista: "))

    except ValueError:
        print("Tente novamente...")
        raise ValueError
    
    try:
        entrada = input("Hora de saída (ex: 07:50): ")
        chegada = input("Hora de chegada (ex: 09:00): ")

        hora_de_saida = FormularioOnibus.tratar_horario(entrada)
        hora_de_chegada = FormularioOnibus.tratar_horario(chegada)

    except ValueError:
        print("Tente novamente...")
        raise ValueError
    
    try:
        roleta_inicial = int(input("Roleta inicial: "))
        roleta_local = int(input("Roleta local: "))

        if roleta_inicial > 99999 and roleta_local > 99999:
            print("Roleta está incorreta...")
            raise ValueError

    except ValueError:
        print("Tente novamente...")
        raise ValueError
    break"""
    
#infos_do_carro = FormularioOnibus(matricula_do_fiscal, ponto_de_controle, dia, numero_da_linha, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local)

