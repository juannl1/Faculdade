from datetime import datetime, timedelta



class FormularioOnibus():
    def __init__(self):
        
        self.matricula_fiscal = None 
        self.numero_da_linha = None
        self.ponto_de_controle = None
        self.numero_do_carro = None
        self.matricula_do_motorista = None
        self.hora_de_saida = None
        self.hora_de_chegada = None
        self.tempo_viagem_total = None
        self.roleta_inicial = None
        self.roleta_local = None
        self.data_anotacao = None
        self.hora_anotacao = None

        pontos_de_contole = ["ESTAÇÃO N.S. MERCÊS (RIO)", "ESTAÇÃO JOÃO BRASIL (NIT)", "ESTAÇÃO N.S. MERCÊS (VOLTA)", "ESTAÇÃO JOÃO BRASIL (VOLTA)", "TRIBOBÓ VOLTA (RIO)", "TRIBOBÓ VOLTA (NIT)", "TRIBOBÓ URB"]
        linhas = ["2144R", "2146D", "4144R", "4146D", "6146D", "2590R"]

        posicao_na_numero_da_linha = numero_da_linha - 1
        self.numero_da_linha = linhas[posicao_na_numero_da_linha]

        posicao_na_lista_pontos_de_controle = ponto_de_controle - 1
        self.ponto_de_controle = pontos_de_contole[posicao_na_lista_pontos_de_controle]


# Métodos

    # Verificar se há pessoas em pé no carro

    def verificar_lotacao(self, roleta_inicial, roleta_local):
        calculo_de_pessoas_no_onibus = roleta_local - roleta_inicial
        calculo_de_pessoas_em_pe = calculo_de_pessoas_no_onibus - 52

        if calculo_de_pessoas_no_onibus > 52:
            print(f"O Ônibus está lotado {calculo_de_pessoas_no_onibus}/52\n{calculo_de_pessoas_em_pe} pessoas em pé")
        
        elif calculo_de_pessoas_no_onibus < 52:
            calculo_vagas = 52 - calculo_de_pessoas_no_onibus 
            print(f"O Ônibus com {calculo_vagas} vagas\n Vagas no Ônibus{calculo_de_pessoas_no_onibus}/52")

        else:
            print("O Ônibus está lotado...\nVagas no Ônibus 52/52")


    def verificar_data(self):
        agora = datetime.now()
        self.data_anotacao = agora.strftime("%d/%m/%Y")
        self.hora_anotacao = agora.strftime("%H:%M:%S")
        
    
    # Verificando quanto tempo demorou para chegar no destino
    def calcular_percurso(self, hora_entrada, hora_chegada):
        # 1. Limpeza e padronização dos inputs
        def limpar(h):
            h = h.replace(":", "").strip()
            return h.zfill(4) # Garante 4 dígitos (ex: "730" vira "0730")

        saida_limpa = limpar(hora_entrada)
        chegada_limpa = limpar(hora_chegada)

        # 2. Converte para objetos datetime para poder calcular
        formato = "%H%M"
        obj_saida = datetime.strptime(saida_limpa, formato)
        obj_chegada = datetime.strptime(chegada_limpa, formato)

        # 3. CALCULA O TEMPO DE VIAGEM
        # Se a chegada for menor que a saída, o codigo quebraria. 
        # Esta parte previne erro caso a viagem passe da meia-noite.
        if obj_chegada < obj_saida:
            duracao = (obj_chegada + timedelta(days=1)) - obj_saida
        else:
            duracao = obj_chegada - obj_saida
        
        # Salva a duração formatada em uma variável (ex: "02:10")
        total_segundos = int(duracao.total_seconds())
        horas = total_segundos // 3600
        minutos = (total_segundos % 3600) // 60
        self.tempo_viagem_total = f"{horas:02d}:{minutos:02d}"
        
        

        # Retornamos os objetos caso você precise usar as horas individualmente depois
        return obj_saida, obj_chegada

    #def salvando_itens():


# INICIANDO FORM


form = FormularioOnibus() # criando objeto
def iniciar_programa():

    while True:
        try:
            matricula_fiscal = int(input("\n\nNúmero da matrícula: ")) # Upgrade futuro: consultar a matrícula no banco de dados(.json)
            form.matricula_fiscal = matricula_fiscal
            break

        except ValueError:
            print("\nInválido\nTente Novamente...\n")

    while True:
        try:
            
            numero_da_linha = int(input("1. 2144R\n2. 2146D\n3. 4144R\n4. 4146D\n5. 6146D\n6. 2590R\nEscolha a linha: "))
            if numero_da_linha in [1 ,2 ,3 ,4 ,5 ,6]:
                form.numero_da_linha = numero_da_linha

                break

            else:
                raise ValueError
            
        except ValueError:
            print("\nInválido\nTente Novamente...\n")

    while True:
        try:

            pontos_de_contole = ["ESTAÇÃO N.S. MERCÊS (RIO)", "ESTAÇÃO JOÃO BRASIL (NIT)", "ESTAÇÃO N.S. MERCÊS (VOLTA)", "ESTAÇÃO JOÃO BRASIL (VOLTA)", "TRIBOBÓ VOLTA (RIO)", "TRIBOBÓ VOLTA (NIT)", "TRIBOBÓ URB"]

            posicao_do_ponto_de_controle = int(input("\n1.ESTAÇÃO N.S. MERCÊS (RIO)\n2.ESTAÇÃO JOÃO BRASIL (NIT)\n3.ESTAÇÃO N.S. MERCÊS (VOLTA)\n4.ESTAÇÃO JOÃO BRASIL (VOLTA)\n5.TRIBOBÓ VOLTA (RIO)\n6.TRIBOBÓ VOLTA (NIT)\nEscolha o ponto de controle: "))

            ponto_de_controle_escolhido = pontos_de_contole[posicao_do_ponto_de_controle]
            
        
            if posicao_do_ponto_de_controle in [1 ,2 ,3 ,4 ,5 ,6]:
                form.ponto_de_controle = posicao_do_ponto_de_controle
                
                break
            else:
                raise ValueError

        except ValueError:
            print("\nInválido\nTente Novamente...\n")

    while True:
        try:
            numero_do_carro = int(input("\nNúmero do carro: "))

            if numero_do_carro <= 500: #supondo que o limite da frota seja 500 carros
                form.numero_do_carro = numero_do_carro
                break

            else:
                raise ValueError
        
        except ValueError:
            print("\nInválido\nTente Novamente...\n")

    while True:
        try:
            
            matricula_do_motorista = int(input("\nMatrícula do motorista: ")) # Upgrade futuro: consultar a matrícula no banco de dados(.json)
            form.matricula_do_motorista = matricula_do_motorista
            break

        except ValueError:
            print("\nInválido\nTente Novamente...\n")

    while True:
        try:
            entrada = input("\nHora de saída (ex: 07:50, 750): ")
            chegada = input("Hora de chegada (ex: 09:00, 900): ")
            
            # 1. Calcule o percurso (que já salva o tempo de viagem)
            form.hora_de_saida, form.hora_de_chegada = form.calcular_percurso(entrada, chegada)
            
            # 2. CHAME A FUNÇÃO AGORA PARA PREENCHER A DATA/HORA DA ANOTAÇÃO
            form.verificar_data()

            print("")
            break

        except ValueError:
            print("\nInválido! Tente novamente...\n")

    while True:
        try:
            roleta_inicial = int(input("\nRoleta Inicial: "))
            roleta_final = int(input("Roleta Final: "))

            form.verificar_lotacao(roleta_inicial, roleta_final)
            break
        except ValueError:
            print("\nInválido! Tente novamente...\n")

    print("----- Relatório -----")
    while True:
        try:

            salvar_infos = str(input(f"Matricula do fiscal: {form.matricula_fiscal}\nPonto de controle: {form.ponto_de_controle}\nNúmero do Carro: {form.numero_do_carro}\nMatrícula do Motorista: {form.matricula_do_motorista}\nHora de saída: {form.hora_de_saida}\nHora de chegada: {form.hora_de_chegada}\nTempo de viagem total: {form.tempo_viagem_total}\nRoleta Inicial: {form.roleta_inicial}\nRoleta Final: {form.roleta_local}\n\nDeseja salvar as informações ? (s/n): ")).lower().strip

            if salvar_infos == "s":
                print("Salvando Informações...")

                


            elif salvar_infos == "n":
                while True:
                    try:
                        decisao = str(input("Deseja refazer? (s/n): ")).lower().strip

                        if decisao == "s":
                            print("Ok")
                            iniciar_programa()

                        elif decisao == "n":
                            print("Ok, finalizando...")
                            exit()

                        else:
                            raise ValueError
                    except ValueError:
                        print("\nResposta Inválida\nTente novamente...")
        except ValueError:
            print("\nResposta Inválida\nTente novamente...")

        




iniciar_programa()