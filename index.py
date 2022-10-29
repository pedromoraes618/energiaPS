while True:
    os.system('cls')
    msg.top()
    print('''\n\033[1m[~+] Menu Principal:\033[m
--------------------------------------------------
[1] Login - Concessionária
[2] Login - Cliente/Gerador
[3] Login - Parceiros comercio/instituições de caridade
[4] Sobre
[5] Sair
    ''')
    print('='*40)
    menu_principal = func.valida_menu()

    if menu_principal == 1:
        while True:
            os.system('cls')
            msg.top()
            menu_concecionaria = input('''\n\033[1m[~+] Area - Login - Concessionária:\033[m
------------------------
[1] Login
[2] Sair
Escolha uma opção: »»»  ''')
            if menu_concecionaria == '1':
                lcs.login_concessionaria()

            elif menu_concecionaria == '2':
                os.system('cls')
                break

    elif menu_principal == 2:
        while True:
            os.system('cls')
            msg.top()

            menu_parceiro = input('''\n\033[1m[~+] Area - Login - Cliente:\033[m
------------------------
[1] Login
[2] Sair
Escolha uma opção: »»»  ''')
            if menu_parceiro == '1':
                lgc.login_cliente()

            elif menu_parceiro == '2':
                os.system('cls')
                break

    elif menu_principal == 3:
        while True:
            os.system('cls')
            msg.top()

            menu_parceiro = input('''\n\033[1m[~+] Area - Login - Parceiro:\033[m
------------------------
[1] Login
[2] Sair
Escolha uma opção: »»»  ''')
            if menu_parceiro == '1':
                lprc.login_parceiro()

            elif menu_parceiro == '2':
                os.system('cls')
                break

    elif menu_principal == 4:
        msg.sobre()
    elif menu_principal == 5:
        os.system('cls')
        print('Volte Sempre!...')
        sleep(1)
        os.system('cls')
        break
    else:
        print('Opção inválida. Tente novamente!')
        sleep(1)
