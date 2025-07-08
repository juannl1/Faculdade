import tkinter as tk
from tkinter import messagebox
import random
import os

# Dados
lista_de_bets = [#Futebol
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
    "Sobre Futsal...\n\nO goleiro-linha entrou em quadra. \n\nO time empatou o jogo ou não?",
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
    "Sobre Surf...\n\nO surfista entrou na onda. \n\nCompletou a manobra ou não?",
    "Sobre Surf...\n\nO atleta pegou uma onda grande. \n\nGanhou nota acima de 8.0 ou não?",
    "Sobre Surf...\n\nO surfista caiu durante a manobra. \n\nConseguiu se recuperar ou não?",
    "Sobre Surf...\n\nO competidor esperou por uma série de ondas a bateria toda. \n\nPegou a melhor onda da bateria ou não?",
    "Sobre Surf...\n\nO surfista tentou um aéreo. \n\nConseguiu completar a manobra ou não?"]
lista_de_odds = {0: ['Sim',2.38, 'Não', 2.26],
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
saldo_na_conta = [random.randint(50, 500) for _ in range(100)]
historico = []
saldo_atual = 0
nome_jogador = ""

# Funções auxiliares
def salvar_saldo_em_arquivo(nome, saldo):
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome}: R${saldo:.2f}\n")

def exibir_ranking():
    if not os.path.exists("ranking.txt"):
        return "Nenhum ranking ainda."
    else:
        with open("ranking.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            ranking_ordenado = sorted(linhas, key=lambda x: float(x.split("R$")[1]), reverse=True)
            return "\n".join(ranking_ordenado)

# Interface gráfica
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aposte Já")
        self.geometry("400x500")

        self.label_nome = tk.Label(self, text="Digite seu nome:")
        self.label_nome.pack(pady=5)

        self.entrada_nome = tk.Entry(self)
        self.entrada_nome.pack(pady=5)

        self.botao_iniciar = tk.Button(self, text="Começar Jogo", command=self.iniciar_jogo)
        self.botao_iniciar.pack(pady=10)

        self.texto_saida = tk.Text(self, height=20, width=50)
        self.texto_saida.pack(pady=10)

        self.botao_sim = tk.Button(self, text="Sim", command=lambda: self.realizar_aposta("Sim"), state="disabled")
        self.botao_nao = tk.Button(self, text="Não", command=lambda: self.realizar_aposta("Não"), state="disabled")
        self.botao_sim.pack(side="left", padx=50)
        self.botao_nao.pack(side="right", padx=50)

    def iniciar_jogo(self):
        global nome_jogador, saldo_atual
        nome_jogador = self.entrada_nome.get().strip().capitalize()
        if not nome_jogador:
            messagebox.showerror("Erro", "Digite um nome válido.")
            return
        saldo_atual = random.choice(saldo_na_conta)
        self.texto_saida.insert(tk.END, f"Bem-vindo(a) {nome_jogador}! Você ganhou R$ {saldo_atual:.2f} de freebet!\n")
        self.sortear_aposta()

    def sortear_aposta(self):
        self.bet_index = random.randint(0, len(lista_de_bets) - 1)
        self.resultado_correto = random.choice(["Sim", "Não"])
        self.texto_saida.insert(tk.END, f"\n{lista_de_bets[self.bet_index]}\n")
        odds = lista_de_odds[self.bet_index]
        self.texto_saida.insert(tk.END, f"Odds - Sim: {odds[1]} | Não: {odds[3]}\n")
        self.botao_sim.config(state="normal")
        self.botao_nao.config(state="normal")

    def realizar_aposta(self, escolha):
        global saldo_atual
        aposta = 10.0  # Valor fixo para simplicidade
        if saldo_atual < aposta:
            self.texto_saida.insert(tk.END, "\nSaldo insuficiente para apostar.\n")
            self.finalizar_jogo()
            return

        saldo_restante = saldo_atual - aposta
        odds = lista_de_odds[self.bet_index]
        ganho = aposta * (odds[1] if escolha == "Sim" else odds[3])
        venceu = escolha == self.resultado_correto

        if venceu:
            saldo_atual = saldo_restante + ganho
            resultado = "Ganhou"
        else:
            saldo_atual = saldo_restante
            resultado = "Perdeu"

        historico.append(f"Aposta: R${aposta:.2f} | Resultado: {resultado} | Saldo: R${saldo_atual:.2f}")
        self.texto_saida.insert(tk.END, f"\nVocê {resultado}! Saldo: R${saldo_atual:.2f}\n")

        if saldo_atual < 5:
            self.finalizar_jogo()
        else:
            self.sortear_aposta()

    def finalizar_jogo(self):
        self.botao_sim.config(state="disabled")
        self.botao_nao.config(state="disabled")
        salvar_saldo_em_arquivo(nome_jogador, saldo_atual)
        self.texto_saida.insert(tk.END, "\n=== Fim de Jogo ===\n")
        self.texto_saida.insert(tk.END, "\nHistórico:\n" + "\n".join(historico) + "\n")
        self.texto_saida.insert(tk.END, "\nRanking:\n" + exibir_ranking())

# Executar app
if __name__ == "__main__":
    app = App()
    app.mainloop()