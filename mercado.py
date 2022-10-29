from unicodedata import numeric
import cadastros as cad
import mensagem as msg
import os
import registro_leituras as rl
import funcao as func

transacoes = []


def transferencias(cod_user, tipo):
    os.system('cls')
    msg.top()
    print('\n\033[1m[~+] Transações:\033[m\n')
    print('MERCADO DE CRÉDITOS ')
    cont = -1
    contrato = cod_user
    dado_origem = func.busca_cliente(contrato)
    # if dado['contrato'] == contrato:
    print('.'*40)
    print(
        f'{dado_origem["contrato"]} - {dado_origem["nome"]}  Crédito Atual: R${dado_origem["credito"]}')
    print('.'*40)
    destinatario = func.valida_codigo_parceiro()
    # for dado_parceiro in cad.parceiro:
    dado_destino = func.busca_parceiro(destinatario)
    if dado_destino != -1:
        # verificar se valor é numérico
        Valor_tranferencia = func.valida_moeda(dado_destino)
        dado_origem['credito'] -= Valor_tranferencia
        dado_destino['credito'] += Valor_tranferencia
        print('Contrato: ', dado_origem['contrato'], 'Nome: ',
              dado_origem['nome'], 'Crédito Atualizado: R$', dado_origem['credito'])
        print('-'*80)
        operacao = {'id': len(transacoes)+1000, 'cod origem': dado_origem['contrato'], 'nome origem': dado_origem['nome'], 'valor': Valor_tranferencia,
                    'cod destino': dado_destino['contrato'], 'nome destino': dado_destino['nome'], 'Credito parceiro': Valor_tranferencia, 'tipo': tipo}
        transacoes.append(operacao)
        print(transacoes)
        print('Operação Realizada com sucesso!')
        input('Pressione qualquer tecla para continuar...')
    else:
        print('='*40)
        print("Parceiro não Cadastrado.....")
        print('='*40)

        input('Pressione tecla ENTER para sair...')


def ganhando_credito(origen, destinatario, valor):
    dado_origem = func.busca_parceiro(origen)
    # if dado['contrato'] == contrato:
    print('.'*40)
    print(
        f'{dado_origem["contrato"]} - {dado_origem["nome"]}')
    print('.'*40)
    dado_destino = func.busca_cliente(destinatario)
    if dado_destino != -1:

        dado_origem['credito'] -= valor
        dado_destino['credito'] += valor
        print('Contrato: ', dado_destino['contrato'], 'Nome: ',
              dado_destino['nome'], 'Crédito Atualizado: R$', dado_destino['credito'])
        print('-'*80)
        operacao = {'id': len(transacoes)+1000, 'cod origem': dado_origem['contrato'], 'nome origem': dado_origem['nome'], 'valor': valor,
                    'cod destino': dado_destino['contrato'], 'nome destino': dado_destino['nome'], 'Credito destino': dado_destino['credito'], 'tipo': 'crédito'}
        transacoes.append(operacao)
        print(transacoes)
        print('Operação Realizada com sucesso!')
    else:
        print('='*40)
        print("Parceiro não Cadastrado.....")
        print('='*40)


def relatorio_transacoes(user, tipo):
    os.system('cls')
    msg.top()
    # print('\n\033[1m[~+] Transações:\033[m')
    # print()
    linha = 1
    if tipo == 'parceiro':
        cliente = (func.busca_parceiro(user))
        titulo = (f'\033[1m{"RELATÓRIO DE TRANSAÇÕES:":^80}\033[m')
        origem = ('cliente')
    else:
        cliente = (func.busca_cliente(user))
        titulo = (f'\033[1m{"RELATÓRIO DE MOVIMENTAÇÕES:":^80}\033[m')
        origem = ('Parceiro')
    print(titulo)
    print()
    print(
        f'Conta Contrato:{cliente["contrato"]}  Nome:{cliente["nome"][0:20]}  Saldo: R${cliente["credito"]:.2f}\n')

    print('_'*80)
    print()
    print(
        f'\033[7;33m        {"Doc":12}{origem:35}{"Valor":>6}{"Operação":>18} \033[m')
    for dado in transacoes:
        if dado['cod origem'] == user:
            linha += 1
            if linha % 2 == 0:
                print(
                    f'\033[7m{linha:<8}{dado["id"]:<12}{dado["nome destino"][0:35]:36}R${dado["valor"]:7.2f} {dado["tipo"]:>13} \033[m')
            else:
                print(
                    f'{linha:<8}{dado["id"]:<12}{dado["nome destino"][0:35]:36}R${dado["valor"]:7.2f} {dado["tipo"]:>13}')
            # print('.'*80)
            #linha += 1
        # print('=-'*40)
        elif dado['cod destino'] == user:
            if linha % 2 == 0:
                print(
                    f'\033[7;42m{linha:<8}{dado["id"]:<12}{dado["nome origem"][0:35]:36}R${dado["valor"]:7.2f} {dado["tipo"]:>13} \033[m')
            else:
                print(
                    f'\033[1;32m{linha:<8}{dado["id"]:<12}{dado["nome origem"][0:35]:36}R${dado["valor"]:7.2f} {dado["tipo"]:>13} \033[m')
        #linha += 1
    print()
    print(f'Fim do Extrado')
    print()
