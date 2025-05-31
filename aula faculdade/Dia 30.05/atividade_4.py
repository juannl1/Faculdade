usuarios = []
while True:
    opçao = input("1. Cadastrar\n2. Login\n3. Sair\n\n: ")

    if opçao == "1":
        user = input("Usuário: ")
        senha = input("Senha: ")
        usuarios[user] = senha
    
    elif opçao == "2":
        user = input("Usuário: ")
        senha = input("Senha: ")

        if user in usuarios and usuarios[user] == senha:
            print("Login Bem Sucedido!!!")
        else:
            print("Usuário ou senha Incorretos")
    elif opçao == "3":
        break