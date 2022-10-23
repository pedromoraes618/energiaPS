import os
import cadastros as cad
import mensagem as msg
import grafico as gr
import funcao as func
import mercado
import registro_leituras as rl


def login_cliente():
    while True:
        contratoDigitao = int(input('Digite o Número contrato: »»»  '))
        tokenDigitado = input('Digite o seu Token: »»»  ')
        for dado in cad.gerador:
            contrato = dado['contrato']
            usuario = dado['nome']
            token = dado['token']
            if (contratoDigitao == contrato):  # consultar no vetor se existe o contrato cadastrado
                encontrouContrato = "true"
                user = dado['nome']
                cod_user = dado['contrato']
                if (tokenDigitado == token):
                    encontrou = usuario  # usuario logado senha e contrato ok! criei uma variavel para guardar o nome do ususario caso logado com sucesso
                else:
                    print("Dados incorretos")
                    # input('Pressione qualquer tecla para continuar...')
                    os.system('cls')
                    break

        if (not 'encontrouContrato' in locals() and not 'encontrou' in locals()):
            print("Dados incorretos")
            input('Pressione qualquer tecla para continuar...')
        elif (not 'encontrouContrato' in locals()):
            print("Contrato incorreto")
            input('Pressione qualquer tecla para continuar...')
        elif (not 'encontrou' in locals()):
            print("Token incorreto")
            input('Pressione qualquer tecla para continuar...')

        if 'encontrou' in locals():  # verificar se retornou algum cliente para o usuário
            while True:
                os.system('cls')
                msg.top()
                print(f'\n{user}, Seja Bem Vindo!')
                menu_cliente = input('''
[#] Area - Clientes/Geradores:
--------------------------------------------------
[1] Consulta de Créditos
[2] Uso de Créditos / Transações
[3] Relatórios
[4] Voltar

Escolha uma opção: »»»  ''')

                if menu_cliente == '1':
                    gr.grafico_cliente(cod_user)
                elif menu_cliente == '2':
                    # Transações com parceiros
                    mercado.transferencias(cod_user)
                    #input('EM CONSTRUÇÃO. Tecle para sair >')
                elif menu_cliente == '3':
                    # Relatorios de transações
                    mercado.impressao_extrato(cod_user)
                    input('EM CONSTRUÇÃO. Tecle para sair >')
                elif menu_cliente == '4':
                    os.system('cls')
                    break
        break
