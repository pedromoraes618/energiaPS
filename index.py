import os
import cadastros as cad
import mensagem as msg
import registro_leituras as rl
import login_cliente as lgc
import login_concessionaria as lcs
import login_parceiro as lprc

def valida_numero():
    while True:
        pesq = input('Escolha uma opção: »»»  ')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
            print('Erro, Insira um valor númérico!')
    return pesquisar

# def valida_numero(pesq):
#     while True:
#         pesq = input('Escolha uma opção: »»»  ')
#         if pesq.isnumeric():
#             pesquisar = (int(pesq))
#             break
#         else:
#             print('Erro, Insira um valor númérico!')
#     return pesquisar


while True:
    os.system('cls')
    msg.top()
    print('''
Menu Principal:
--------------------------------------------------
[1] Login - Concessionária
[2] Login - Cliente/Gerador
[3] Login - Parceiros comercio/instituições de caridade
[4] Sobre
[5] Sair
    ''')
    print('='*40)
    menu_principal = valida_numero()

    # menu_principal = int(input('Escolha uma opção: »»»  '))
    # valida_numero(menu_principal)

    if menu_principal == 1:
        while True:
            os.system('cls')
            msg.top()
            menu_concecionaria = input('''
[#] Area - Login/Concessionária:
------------------------
[1] Login
[2] Voltar
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
        
            menu_parceiro = input('''
[#] Area - Login/Cliente:
------------------------
[1] Login
[2] Voltar
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
        
            menu_parceiro = input('''
[#] Area - Login/Parceiro:
------------------------
[1] Login
[2] Voltar
Escolha uma opção: »»»  ''')
            if menu_parceiro == '1':
                lprc.login_parceiro()
            
            elif menu_parceiro == '2':
                os.system('cls')
                break
     
    elif menu_principal == 4:
            print('Informação sobre o projeto - em contrução')
            msg.sobre()
    elif menu_principal == 5:
        os.system('cls')
        print('saindo...')
        break
    else:
        print(f'({menu_principal}) - Opção inválida! ')
        menu_principal = valida_numero()