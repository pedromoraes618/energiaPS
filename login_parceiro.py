import os
import cadastros as cad
import mensagem as msg
import funcao as func
import registro_leituras as rl


def login_parceiro():
    while True:
        usuarioDigitado = input('Digite o seu Usuário: »»»  ')
        tokenDigitado = input('Digite o seu Token: »»»  ')
        for dado in cad.parceiro:
            usuario = dado['user']
            token = dado['token']
            # consultar no vetor se existe o contrato cadastrado
            if (usuarioDigitado == usuarioDigitado):
                encontrouUser = "true"
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
[#] Area - Parceiros comercio/instituições de caridade:
--------------------------------------------------
[1] Relatórios de transações
[2] Uso de créditos
[3] Voltar
Escolha uma opção: »»»  ''')
                if menu_parceiro == '1':
                    input('EM CONSTRUÇÃO. Tecle para sair >')
                elif menu_parceiro == '2':
                    input('EM CONSTRUÇÃO. Tecle para sair >')
                elif menu_parceiro == '3':
                    os.system('cls')
                    break

        break
