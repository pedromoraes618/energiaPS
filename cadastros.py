'''Contrato – unidade consumidora
Nome – pessoa dona da conta contrato
Consumido – o consumo de energia realizado pela casa
Injetado – a anergia gerada pelas placas solares
Saldo_energetico
Consersor - (%) do saldo_energetico
Credito - conversor do saldo_energetico'''
import os
import mensagem as msg
import grafico
import funcao as fun
from random import randint, random

def valida_num(pesq):
    while True:
        pesq = input('Digite a Matrícula do Aluno:')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
            msg.erro_numerico()
    return pesquisar


cotacao =[9]

gerador = [{'contrato': '123', 'nome': 'Cristiano Ronaldo', 'consumido': 400, 'injetado': 500, 'saldo_energetico': 100, 'conversor': cotacao[0], 'credito': 40,'token':'0'},
           {'contrato': '122', 'nome': 'Messi', 'consumido': 400, 'injetado': 500,'saldo_energetico': 100,'conversor': cotacao[0], 'credito': 60,'token':'0'},
           {'contrato': '121', 'nome': 'Ronaldinho Gaucho', 'consumido': 600,'conversor': cotacao[0], 'injetado': 900, 'saldo_energetico': 300, 'credito': 270,'token':'0'}]


parceiro = [{'contrato': '1', 'nome': 'Supermercado', 'tipo': 'comercio', 'credito': 0,'user':'adm2','token':'145'}, {
    'contrato': 2, 'nome': 'Farmácia', 'tipo': 'comercio', 'credito': '0','user':'adm3','token':'155'}]

concecionaria = [{'user': 'adm', 'token': '165'},{'user': 'adm1', 'token': '0'}]


# def parceria():
#     while True:
#         tipo_parceiro = input(
#             '[1] - Comercio / [2] - Instituição de Caridade: ')
#         if tipo_parceiro == '1':
#             tipo_parceiro = 'comercio'
#             break
#         elif tipo_parceiro == '2':
#             tipo_parceiro = 'caridade'
#             break
#         elif tipo_parceiro:
#             print('Verifique as opções!!!')

def cadastro_parceiro():
    print('\nCADASTRO DE PARCEIROS:\n')
    contrato = len(parceiro)+1
    nome = str(input('Digite o Nome da Empresa:'))
    while True:
        tipo_parceiro = input(
            ' [c] Comercio / [i] - Instituição de Caridade: ').lower()[0]
        if tipo_parceiro == 'c':
            tipo_parceiro = 'comercio'
            break
        elif tipo_parceiro == 'i':
            tipo_parceiro = 'caridade'
            break
        elif tipo_parceiro:
            print('Verifique as opções!!!')
    credito = 0
    dados_comercio = {'contrato': contrato, 'nome': nome,
                      'tipo': tipo_parceiro, 'credito': credito}
    parceiro.append(dados_comercio)
    relatorio_parceiro()


def cadastro_geradores():
    while True:
        contrato = fun.validaNumeroContrato()  ##validar numero contrato para aceitar apenas numero
        nome = str(input('Digite o nome do cliente:'))
        token = randint(1,10000000) ##gerar token
        token = (str(token))
        while True:
                alert = input("Deseja cadastrar esse cliente? tecle s ou n: ")
                if alert =="s":
                    print("Token gerado para cliente: ",token,"o token será enviado para o cliente via email")
                    consumido = 0  # int(input('Valor consumido(KWh):'))
                    injetado = 0  # int(input('Valor injetado(KWh):'))
                    saldo_energetico = 0
                    conversor = 0.9
                    credito = 0
                    dados_gerador = {'contrato': contrato, 'nome': nome, 'consumido': consumido, 'injetado': injetado,
                                    'saldo_energetico': saldo_energetico, 'conversor': conversor, 'credito': credito,'token':token}
                    gerador.append(dados_gerador)
                    print('='*40)
                    input('Cadastro realizado com sucesso! Pressione qualquer tecla para continuar...')
                    print('='*40)
                    break
                elif alert =="n":
                    input('Operação cancelada! Pressione qualquer tecla para continuar...')
                    break
                else:
                    input('Erro, Pressione qualquer tecla para continuar... ')
                    break       
              
        break

def consultar_geradores():
    while True:
        contrato = (input('Digite a conta contrato:'))
        for dado in gerador:
            consulta = dado['contrato']
            if(consulta == contrato): #consultar no vetor se existe o contrato cadastrado
                print('='*40)
                print('Contrato:', dado['contrato'], ' Nome:', dado['nome'],'Token:',dado['token'],'Consumido',dado['consumido'])
                encontrou = "true"
                print('='*40)
                    
        if not 'encontrou' in locals():  #verificar se retornou algum cliente para o usuário
            print('='*40)
            print("Cliente/Gerador não encontrado.....")
            print('='*40)

        input('Pressione qualquer tecla para continuar...')
        break

def relatorio_geradores():
    for dado in gerador:
        print('Contrato: ', dado['contrato'], 'Nome: ', dado['nome'])
        print('Energ. Consumida:', dado['consumido'], 'Energ. Injetada: ',
              dado['injetado'], 'Saldo Disponível: ', dado['saldo_energetico'], 'Crédito: E$', dado['credito'])
        print('-'*80)
    input('Pressione qualquer tecla para continuar...')


# def grafico_geradores():
#     os.system('cls')
#     msg.top()
#     print('\nRelatório de Clientes Geradores\n')
#     for dado in gerador:
#         print('Contrato: ', dado['contrato'], 'Nome: ',
#               dado['nome'], ' Crédito:', dado['credito'])
#         print(f'{"Energ. Consumida:":20} {dado["consumido"]:<5}', end=' ')
#         cons = (dado["consumido"])//10
#         print('\033[1;41m \033[m'*cons)
#         print(f'{"Energ. Injetada:":20} {dado["injetado"]:<5}', end=' ')
#         cons = (dado["injetado"])//10
#         print('\033[1;42m \033[m'*cons)
#         print('-'*100)
#     input('Pressione qualquer tecla para continuar...')


def grafico_cliente():
    os.system('cls')
    msg.top()
    print('\nGráfico de Clientes Geradores\n')
    for dado in gerador:
        # if dado['contrato'] == 123:
        print('Contrato: ', dado['contrato'], 'Nome: ',
              dado['nome'], ' Crédito:', dado['credito'])
        print(f'{"Energ. Consumida:":20} {dado["consumido"]:<5}', end=' ')
        consC = (dado["consumido"])//100
        consI = (dado["injetado"])//100
        grafico.grafico_vertical(consI, consC)

    input('Pressione qualquer tecla para continuar...')


def relatorio_parceiro():
    os.system('cls')
    msg.top()
    print('Relatório de Parceiros Cadastrados')
    for dado in parceiro:
        print('Contrato:', dado['contrato'], 'Nome:',
              dado['nome'], 'Crédito:', dado['credito'], 'Tipo de Parceiro:', dado['tipo'])
        print('.'*100)
    input('Pressione qualquer tecla para continuar...')


# def editar():
#     contrato = int(input('Digite a Conta Contrado: '))
#     for k, v in gerador:
#         print(f'{k:>10} | {v}')


# print(gerador)

def editar_cotacao():
    print("Valor atual da cotação ",cotacao[0])
    print('='*40)
    cotacaoValor = fun.editaCotacao()
    cotacao[0] = cotacaoValor
    print('='*40)
    print("Ajuste realizado, novo valor de cotação ",cotacao[0])
    input("Valor atualizado!Pressione qualquer tecla para continuar...")
 