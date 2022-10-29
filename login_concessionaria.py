import os
import cadastros as cad
import mensagem as msg
import funcao as func
import registro_leituras as rl
from getpass import getpass


def login_concessionaria():
    while True:
        usuarioDigitado = str(input('Digite o seu Usuário: »»»  '))
        tokenDigitado = getpass(
            prompt='Digite o seu Token: »»»  ')
        for dado in cad.concecionaria:
            usuario = dado['user']
            token = dado['token']
            # consultar no vetor se existe o contrato cadastrado
            if(usuarioDigitado == usuario):
                encontrouUser = "true"
                if(tokenDigitado == token):
                    encontrou = usuario  # usuario logado senha e contrato ok! criei uma variavel para guardar o nome do ususario caso logado com sucesso
                else:
                    print("Dados incorretos")
                    # input('Pressione qualquer tecla para continuar...')
                    os.system('cls')
                    break

        if(not 'encontrouUser' in locals() and not 'encontrou' in locals()):
            print("Dados incorretos")
            input('Pressione qualquer tecla para continuar...')
            break
        elif(not 'encontrouUser' in locals()):
            print("Usuário incorreto")
            input('Pressione qualquer tecla para continuar...')
            break
        elif(not 'encontrou' in locals()):
            print("Token incorreto")
            input('Pressione qualquer tecla para continuar...')
            break

        if 'encontrou' in locals():  # verificar houve retorno para o usuário
            while True:
                os.system('cls')
                msg.top()
                menu_concessionaria = input('''\n\033[1m[~+] Area - Concessionária:\033[m
--------------------------------------------------
[1] Cadastro Clientes/Geradores
[2] Cadastro Parceiros
[3] Registro de Leituras
[4] Relatórios
[5] Consultar Clientes/Geradores
[6] Alterar cotação $
[7] Sair

Escolha uma opção: »»»  ''')
                if menu_concessionaria == '1':
                    cad.cadastro_clientes()
                elif menu_concessionaria == '2':
                    os.system('cls')
                    msg.top()
                    cad.cadastro_parceiro()
                elif menu_concessionaria == '3':
                    rl.registro()
                elif menu_concessionaria == '4':
                    while True:
                        os.system('cls')
                        msg.top()
                        menu_relatorio_concessionaria = input('''\n\033[1m[~+] Menu Concessionária Relatórios:\033[m
--------------------------------------------------
[1] Relatório de Clientes
[2] Relatório de Parceiros
[3] Sair
Escolha uma opção: »»»  ''')
                        if menu_relatorio_concessionaria == '1':
                            cad.relatorio_clientes()
                        if menu_relatorio_concessionaria == '2':
                            cad.relatorio_parceiro()
                        if menu_relatorio_concessionaria == '3':
                            os.system('cls')
                            break
                elif menu_concessionaria == '5':
                    cad.consultar_clientes()

                elif menu_concessionaria == '6':
                    cad.editar_cotacao()

                elif menu_concessionaria == '7':
                    os.system('cls')
                    break
            break
