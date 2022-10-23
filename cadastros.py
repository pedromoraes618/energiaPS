'''Contrato – unidade consumidora
Nome – pessoa dona da conta contrato
Consumido – o consumo de energia realizado pela casa
Injetado – a anergia gerada pelas placas solares
Saldo_energetico
Consersor - (%) do saldo_energetico
Credito - cotacao do saldo_energetico'''
import os
import mensagem as msg
import grafico as gf
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


def editar_cotacao():
    cotacao = vCotacao[0]
    print('='*40)
    print("Valor atual da cotação ", gerador[0]['cotacao'])
    cotacao = float(input('Digite o novo valor da cotação: '))
    print('='*40)
    print("Ajuste realizado, novo valor de cotação ", cotacao)
    input("Valor atualizado!Pressione qualquer tecla para continuar...")
    # atualizando lista geradores
    for dado in gerador:
        dado['cotacao'] = cotacao
        dado['credito'] = dado['saldo_energetico'] * cotacao
        # break


vCotacao = [0.9]  # editar_cotacao()

gerador = [{'contrato': 100, 'nome': 'CRISTIANO RONALDO', 'consumido': 400, 'injetado': 600, 'saldo_energetico': 200, 'cotacao': 0.9, 'credito': 180, 'token': '0'},
           {'contrato': 101, 'nome': 'MESSI', 'consumido': 400, 'injetado': 500,
               'saldo_energetico': 100, 'cotacao': 0.9, 'credito': 90, 'token': '0'},
           {'contrato': 102, 'nome': 'RONALDINHO GAUCHO', 'consumido': 600, 'cotacao': 0.9, 'injetado': 900, 'saldo_energetico': 300, 'credito': 270, 'token': '0'}]


parceiro = [{'contrato': 1, 'nome': 'Supermercado', 'tipo': 'comercio', 'credito': 0.0, 'user': 'adm2', 'token': '145'}, {
    'contrato': 2, 'nome': 'Farmácia', 'tipo': 'comercio', 'credito': 0.0, 'user': 'adm3', 'token': '155'}]

concecionaria = [{'user': 'adm', 'token': '165'},
                 {'user': 'adm1', 'token': '0'}]


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
    # while True:
    os.system('cls')
    msg.top()
    print('\n\033[1mCADASTRO DE CLIENTES/GERADORES\033[m')
    # validar numero contrato para aceitar apenas numero
    #contrato = fun.validaNumeroContrato()
    contrato = len(gerador)+100
    nome = str(input('\nDigite o nome do cliente: ')).upper()
    token = randint(1, 10000000)  # gerar token
    token = (str(token))
    while True:
        alert = input("Deseja cadastrar esse cliente? (s/n): ")[0]
        if alert in 'sS':  # alert == "s" or alert == 'S':
            print("Token gerado para cliente: ", token,
                  "o token será enviado para o cliente via email")
            consumido = 0  # int(input('Valor consumido(KWh):'))
            injetado = 0  # int(input('Valor injetado(KWh):'))
            saldo_energetico = 0
            cotacao = [0]  # teste (arranjo tecnico)
            credito = 0.0
            dados_gerador = {'contrato': contrato, 'nome': nome, 'consumido': consumido, 'injetado': injetado,
                             'saldo_energetico': saldo_energetico, 'cotacao': cotacao, 'credito': credito, 'token': token}
            gerador.append(dados_gerador)
            print('='*40)
            input(
                'Cadastro realizado com sucesso! Pressione qualquer tecla para continuar...')
            print('='*40)
            break
        elif alert in 'nN':  # alert == "n" or alert == 'N':
            input('Operação cancelada! Pressione qualquer tecla para continuar...')
            break
        else:
            input(
                ' Tecle S para salvar ou N para cancelar a operação. \n Pressione qualquer tecla para continuar... ')
            # break

        # break


def consultar_geradores():
    while True:
        os.system('cls')
        msg.top()
        contrato = int(input('Digite a conta contrato:'))
        for dado in gerador:
            consulta = dado['contrato']
            if(consulta == contrato):  # consultar no vetor se existe o contrato cadastrado
                print('='*40)
                print('Contrato:', dado['contrato'], ' Nome:', dado['nome'],
                      'Token:', dado['token'], 'Consumido', dado['consumido'])
                encontrou = "true"
                print('='*40)
                gf.grafico_horizontal(dado['contrato'])

        if not 'encontrou' in locals():  # verificar se retornou algum cliente para o usuário
            print('='*40)
            print("Cliente/Gerador não encontrado.....")
            print('='*40)

        input('Pressione qualquer tecla para continuar...')
        break


def relatorio_geradores():
    os.system('cls')
    msg.top()
    print('\n\033[1mRELATÓRIO DE CLIENTES/GERADORES\033[m\n')
    for dado in gerador:
        print('Contrato: ', dado['contrato'], 'Nome: ', dado['nome'])
        print('Energ. Consumida:', dado['consumido'], 'Energ. Injetada: ',
              dado['injetado'], 'Saldo Disponível: ', dado['saldo_energetico'], 'Crédito: R$', dado['credito'])
        print('-'*80)
    input('Pressione qualquer tecla para continuar...')


def relatorio_parceiro():
    os.system('cls')
    msg.top()
    print('\n\033[1mRelatório de Parceiros Cadastrados\033[m\n')
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
