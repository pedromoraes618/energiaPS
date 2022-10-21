import os
import cadastros as cad
import mensagem as msg
import funcao as func
import registro_leituras as rl


def login_cliente():
    while True:
        contratoDigitao = input('Digite o Número contrato: »»»  ')
        tokenDigitado = input('Digite o seu Token: »»»  ')
        for dado in cad.gerador:
            contrato = dado['contrato']
            usuario = dado['nome']
            token = dado['token']
            if (contratoDigitao == contrato):  # consultar no vetor se existe o contrato cadastrado
                encontrouContrato = "true"
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
                menu_cliente = input('''
[#] Area - Clientes/Geradores:
--------------------------------------------------
[1] Consulta de Créditos
[2] Uso de Créditos / Transações
[3] Relatórios
[4] Voltar

Escolha uma opção: »»»  ''')

                if menu_cliente == '1':
                    cad.grafico_cliente()
                elif menu_cliente == '2':
                    # Transações com parceiros
                    input('EM CONSTRUÇÃO. Tecle para sair >')
                elif menu_cliente == '3':
                    # Relatorios de transações
                    input('EM CONSTRUÇÃO. Tecle para sair >')
                elif menu_cliente == '4':
                    os.system('cls')
                    break
        break
