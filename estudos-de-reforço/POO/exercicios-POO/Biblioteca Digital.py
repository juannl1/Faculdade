class Livro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.status_lido = False 

    def marcar_como_lido(self):
        status = input(f"Deseja marcar '{self.titulo}' como lido? (s/n) > ").strip().lower()
        if status == "s":
            self.status_lido = True

class Biblioteca():
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"✅ Livro '{livro.titulo}' guardado na estante!")
        
    def listar_livros(self):
        print("\n" + "="*30)
        print("Sua Biblioteca Digital")
        print("="*30)
        if not self.acervo:
            print("A biblioteca está vazia.")
        for livro in self.acervo:
            status = "✅ Lido" if livro.status_lido else "❌ Não lido"
            print(f"📖 {livro.titulo.ljust(25)} | Autor: {livro.autor.ljust(15)} | {status}")
        print("="*40)





#iniciando programa

minha_biblioteca = Biblioteca()
nome_do_cliente = input("Digite seu nome completo > ").title()

while True:
    print("\n--- Cadastro de Novo Livro ---")
    titulo = input("Título do Livro: ")
    autor = input("Autor do Livro: ")
    paginas = int(input("Número de páginas: "))

    
    novo_livro = Livro(titulo, autor, paginas)
    
    
    novo_livro.marcar_como_lido()
    
    
    minha_biblioteca.adicionar_livro(novo_livro)

    
    continuar = input("\nDeseja adicionar outro livro? (s/n) > ").strip().lower()
    if continuar != 's':
        break

minha_biblioteca.listar_livros()
print(f"\nAté logo, {nome_do_cliente.split()[0]}!")