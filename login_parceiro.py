import os
import cadastros as cad
import mensagem as msg
import funcao as func
import registro_leituras as rl
import mercado
from getpass import getpass


def login_parceiro():
    while True:

        # int(input('Digite o seu Usuário: »»»  '))
        usuarioDigitado = func.validaNumeroContrato()
        tokenDigitado = getpass(
            prompt='Digite o seu Token: »»»  ')
        for dado in cad.parceiro:
            # consultar no vetor se existe o contrato cadastrado
            if (usuarioDigitado == dado['contrato']):
                usuario = dado['nome']
                token = dado['token']
                encontrouUser = "true"
                user = dado['nome']
                cod_user = dado['contrato']
                if (tokenDigitado == token):
                    encontrou = usuario  # usuario logado senha e contrato ok! criei uma variavel para guardar o nome do ususario caso logado com sucesso
                else:
                    print("Dados incorretos")
                    # input('Pressione qualquer tecla para continuar...')
                    os.system('cls')
                    break

        if (not 'encontrouUser' in locals() and not 'encontrou' in locals()):
            print("Dados incorretos")
            input('Pressione qualquer tecla para continuar...')
        elif (not 'encontrouUser' in locals()):
            print("Usuário incorreto")
            input('Pressione qualquer tecla para continuar...')
        elif (not 'encontrou' in locals()):
            print("Token incorreto")
            input('Pressione qualquer tecla para continuar...')

        if 'encontrou' in locals():  # verificar houve retorno para o usuário
            while True:
                os.system('cls')
                msg.top()
                menu_parceiro = input('''
[~+] Area - Parceiros comercio/instituições de caridade:
--------------------------------------------------
[1] Relatórios de transações
[2] Uso de créditos 
[3] Voltar
Escolha uma opção: »»»  ''')
                if menu_parceiro == '1':
                    mercado.relatorio_transacoes(cod_user, 'parceiro')
                    input('Tecle ENTER para sair >')
                elif menu_parceiro == '2':
                    input('Tecle ENTER para sair >')
                elif menu_parceiro == '3':
                    os.system('cls')
                    break
        break
