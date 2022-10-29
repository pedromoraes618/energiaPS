import os
import cadastros as cad
import login_cliente as lgc
import mensagem as msg
import registro_leituras as rl


def valida_menu():

    while True:
        pesq = input('Escolha uma opção: »»»  ')
        if pesq.isnumeric():
            pesquisar = (int(pesq))
            break
        else:
            print('Erro, Insira um valor numérico!')
    return pesquisar


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


def valida_moeda(dado_destino):
    while True:
        Valor_tranferencia = input(
            f'Qual é o valor da tranferência para \033[1m{dado_destino["nome"]}\033[m: R$')
        if Valor_tranferencia.isnumeric():
            Valor_tranferencia = (float(Valor_tranferencia))
            if Valor_tranferencia > 0.01:
                break
            else:
                print('Valor inválido!')
        else:
            print('Valor digita é inválido')
    return Valor_tranferencia


def busca_cliente(cliente):
    while True:
        contrato = cliente
        for dado in cad.clientes:
            consulta = dado['contrato']
            if(consulta == contrato):  # consultar no vetor se existe o contrato cadastrado
                return dado

        if not 'encontrou' in locals():  # verificar se retornou algum cliente para o usuário
            return -1


def busca_clientes(cliente):
    while True:
        contrato = cliente
        for dado in cad.clientes:
            consulta = dado['contrato']
            if(consulta == contrato):  # consultar no vetor se existe o contrato cadastrado
                return dado

        if not 'encontrou' in locals():  # verificar se retornou algum cliente para o usuário
            return -1


def busca_parceiro(cod_parceiro):
    while True:
        contrato = cod_parceiro
        for dado in cad.parceiro:
            consulta = dado['contrato']
            if(consulta == contrato):  # consultar no vetor se existe o contrato cadastrado
                return dado

        if not 'encontrou' in locals():  # verificar se retornou algum parceiro para o usuário
            return -1


def verificar_nome(tipo):
    while True:
        nome = str(input(f'\nDigite o nome do {tipo}:')).upper()
        for c in nome:
            if c != ' ':
                return nome
        else:
            print('Campo com tamanho insuficiente!')


def verificar_s_n(tipo):
    while True:
        alert = input(tipo)
        for c in alert:
            if c != ' ':
                return alert[0]
        else:
            print('Campo sem valor!')
