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
        pesq = input('Digite a conta contrato:')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
            msg.erro_numerico()
    return pesquisar


def editar_cotacao():
    os.system('cls')
    msg.top()
    print()
    print('\033[1m[~+] Area - Concessionária:\033[m\n')
    print('\033[1mATUALIZAÇÃO DE COTAÇÃO DE CRÉDITO:\033[m\n')
    print('='*40)
    print("Valor atual da cotação ", vCotacao)
    vCotacao.append(float(input('Digite o novo valor da cotação: ')))
    print('='*40)
    print(f'Novo valor: 1 cédito vale R${vCotacao[len(vCotacao)-1]}')
    input("Valor atualizado!Pressione  tecla ENTER para continuar...")
    # atualizando lista clienteses
    for dado in clientes:
        #dado['cotacao'] = cotacao
        dado['credito'] = dado['saldo_energetico'][len(
            dado['saldo_energetico'])-1] * vCotacao[len(vCotacao)-1]
        # break


vCotacao = [0.9]  # editar_cotacao()

clientes = [{'contrato': 100, 'nome': 'CRISTIANO RONALDO', 'consumido': [700, 600, 700, 750], 'injetado': [900, 850, 800, 820], 'saldo_energetico': [200, 250, 100, 70], 'credito': 558, 'token': '0'},
            {'contrato': 101, 'nome': 'MESSI', 'consumido': [0], 'injetado': [0],
             'saldo_energetico': [0],  'credito': 165, 'token': '0'},
            {'contrato': 102, 'nome': 'RONALDINHO GAUCHO', 'consumido': [600, 500, 400, 450],  'injetado': [900, 850, 800, 820], 'saldo_energetico': [300, 350, 400, 370], 'credito': 1278, 'token': '0'}]


parceiro = [{'contrato': 0, 'nome': 'Equatorial', 'tipo': 'concessionaria', 'credito': 0.0, 'user': 'adm1', 'token': '145'}, {
    'contrato': 1, 'nome': 'Farmácia', 'tipo': 'comercial', 'credito': 0.0, 'user': 'adm3', 'token': '155'},
    {'contrato': 2, 'nome': 'Supermercado', 'tipo': 'comercial',
        'credito': 0.0, 'user': 'adm2', 'token': '165'},
    {'contrato': 3, 'nome': 'hospital do cancer', 'tipo': 'caridade', 'credito': 0.0, 'user': 'adm2', 'token': '175'}]


concecionaria = [{'user': 'adm', 'token': '165'},
                 {'user': 'adm1', 'token': '0'}]


def cadastro_parceiro():
    print('\n\033[1m[~+] Area - Concessionária:\033[m\n')
    print('\n\033[1mCADASTRO DE PARCEIROS:\033[m\n')
    contrato = len(parceiro)+1
    nome = fun.verificar_nome('da Empresa')
    token = randint(10, 99)  # gerar token
    token = (str(token))
    while True:
        tipo_parceiro = fun.verificar_s_n(
            '[c] Comercio / [i] - Instituição de Caridade: ')
        if tipo_parceiro in 'Cc':
            tipo_parceiro = 'comercial'
            break
        elif tipo_parceiro in 'Ii':
            tipo_parceiro = 'caridade'
            break
        else:
            print('Verifique as opções!!!')

    while True:
        #alert = input("Deseja cadastrar esse parceiro? (s/n): ")
        alert = fun.verificar_s_n('Deseja cadastrar esse parceiro? (s/n): ')
        if alert in 'sS':
            credito = 0
            dados_comercio = {'contrato': contrato, 'nome': nome,
                              'tipo': tipo_parceiro, 'credito': credito, 'token': token}
            parceiro.append(dados_comercio)
            print(
                f'Token gerado para o Parceiro: {contrato}-{nome}.\n(Token, \033[4m{token}\033[m, será enviado via email)\n')

            input(
                'Cadastro realizado com sucesso! Pressione tecla ENTER para sair...')
            print('='*40)
            break
        elif alert in 'nN':
            input('Operação cancelada! Pressione tecla ENTER para sair...')
            break
        else:
            print(
                ' Tecle S para salvar ou N para cancelar a operação.')


def consultar_clientes():
    while True:
        os.system('cls')
        msg.top()
        contrato = fun.validaNumeroContrato()
        # contrato = int(input('Digite a conta contrato:'))
        for dado in clientes:
            consulta = dado['contrato']
            if(consulta == contrato):  # consultar no vetor se existe o contrato cadastrado
                print('='*40)
                print('Contrato:', dado['contrato'], ' Nome:', dado['nome'],
                      'Credito', dado['credito'])
                encontrou = "true"
                print('='*40)
                gf.grafico_horizontal(dado['contrato'])

        if not 'encontrou' in locals():  # verificar se retornou algum cliente para o usuário
            print('='*40)
            print("Cliente/Gerador não encontrado.....")
            print('='*40)

        input('Pressione tecla ENTER para continuar...')
        break


def relatorio_clientes():
    os.system('cls')
    msg.top()
    print('\n\033[1m[~+] Area - Concessionária:\033[m\n')
    print('\n\033[1mRELATÓRIO DE CLIENTES\033[m\n')
    for dado in clientes:
        print(f'Contrato: {dado["contrato"]}    Nome: {dado["nome"]}')
        print(
            f'Energ. Consumida: {dado["consumido"][len(dado["consumido"])-1]}kWh     Energ. Injetada: {dado["injetado"][len(dado["injetado"])-1]}kWh     Saldo Disponível:{dado["saldo_energetico"][len(dado["saldo_energetico"])-1]}kWh     Crédito: R$ {dado["credito"]}')
        print('-'*100)
    input('Pressione  tecla ENTER para voltar...')


def relatorio_parceiro():
    os.system('cls')
    msg.top()
    print('\n\033[1mRelatório de Parceiros Cadastrados\033[m\n')
    for dado in parceiro:
        print(f'Contrato: {dado["contrato"]} Nome: {dado["nome"][0:30]}')
        print(f'Crédito: {dado["credito"]} Tipo de Parceiro: {dado["tipo"]}')
        print('.'*100)
    input('Pressione tecla ENTER para voltar...')


def cadastro_clientes():
    os.system('cls')
    msg.top()
    print('\n\033[1m[~+] Area - Concessionária:\033[m')
    print('.'*30)
    print('\n\033[1mCADASTRO DE CLIENTES\033[m')
    contrato = len(clientes)+100
    nome = fun.verificar_nome('do cliente')
    token = randint(1000, 9999)  # gerar token
    token = (str(token))
    while True:
        #alert = input("Deseja cadastrar esse cliente? (s/n): ")[0]
        alert = fun.verificar_s_n('Deseja cadastrar esse cliente? (s/n): ')
        if alert in 'sS':
            print(
                f'Token gerado para cliente: {contrato}-{nome}. (Token, {token}, será enviado via email')
            consumido = [0]
            injetado = [0]
            saldo_energetico = [0]
            # cotacao = [0]  # teste (arranjo tecnico)
            credito = 0.0
            dados_cliente = {'contrato': contrato, 'nome': nome, 'consumido': consumido, 'injetado': injetado,
                             'saldo_energetico': saldo_energetico, 'credito': credito, 'token': token}
            clientes.append(dados_cliente)
            print('='*40)
            input(
                'Cadastro realizado com sucesso! Pressione tecla ENTER para sair...')
            print('='*40)
            break
        if alert in 'nN':
            input('Operação cancelada! Pressione tecla ENTER para sair...')
            break
        else:
            input(
                ' Tecle S para salvar ou N para cancelar a operação. \n Pressione  tecla ENTER para sair... ')
