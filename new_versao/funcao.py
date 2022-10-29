
import os
import cadastros as cad
import login_cliente as lgc
import mensagem as msg
import registro_leituras as rl

# validar numero contrato para aceitar apenas numero


def validaNumeroContrato():
    while True:
        pesq = input('Digite o Número contrato: »»»  ')
        if pesq.isnumeric():
            pesq = (int(pesq))
            break
        else:
            print('Erro, Insira um valor númérico(Número contrato): ')
    return pesq

# validar toen para aceitar apenas numero


def validaToken():
    while True:
        pesq = input('Digite o seu Token: »»»  ')
        if pesq.isnumeric():
            break
        else:
            print('Erro, Insira um valor númérico(Token:): ')
    return pesq


def editaCotacao():
    while True:
        cotacao = input('Digite o novo valor(0-10): »»»  ')
        if cotacao.isnumeric():
            cotacao = (float(cotacao))
            break
        else:
            print('Erro, Insira um valor númérico(0-10)!')
    return cotacao

def valida_consumo():
    while True:
        pesq = input('Leitura de consumo(kWh):')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
          print("Erro, tente novamente")
    return pesquisar


def valida_valor_injetado():
    while True:
        pesq = input('Leitura de valor injetado(kWh):')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
          print("Erro, tente novamente")
    return pesquisar

def valida_codigo_parceiro():
    while True:
        pesq = input('Código do Parceiro: ')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
          print("Erro, tente novamente")
    return pesquisar
    # def busca_cliente(contrato):
    #     for dado in cad.gerador:
    #         if contrato == dado['contrato']:
    #             return


# def busca_geradores(cliente):
#     while True:
#         contrato = cliente
#         for dado in cad.gerador:
#             consulta = dado['contrato']
#             if(consulta == contrato):  # consultar no vetor se existe o contrato cadastrado
#                 return contrato

#         if not 'encontrou' in locals():  # verificar se retornou algum cliente para o usuário
#             print('='*40)
#             print("Cliente/Gerador não encontrado.....")
#             print('='*40)

#         input('Pressione  tecla ENTER para continuar...')
#         break
