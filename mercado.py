import cadastros as cad
import mensagem as msg
import os

extrato = []


def transferencias(cod_user):
    os.system('cls')
    msg.top()
    print('MERCADO DE CRÉDITOS ')
    cont = -1
    repetir = 's'
    # tempDado.clear()
    # while repetir == 's':
    # dado.clear()
    contrato = cod_user
    for dado in cad.gerador:
        cont = cont+1

        if dado['contrato'] == contrato:
            print('.'*40)
            print(f'{dado["nome"]}  Crédito Atual:{dado["credito"]}')
            print('.'*40)
            destinatario = int(input('Código do Parceiro: '))
            for dado_parceiro in cad.parceiro:
                if dado_parceiro['contrato'] == destinatario:
                    Valor_tranferencia = float(input(
                        f'Qual é o valor da tranferência para \033[1m{dado_parceiro["nome"]}\033[m: R$'))
                    dado['credito'] -= Valor_tranferencia
                    dado_parceiro['credito'] += Valor_tranferencia
                    print('Contrato: ', dado['contrato'], 'Nome: ',
                          dado['nome'], 'Crédito Atualizado: R$', dado['credito'])
                    print('-'*80)
                    operacao = {'contrato': dado['contrato'], 'cliente': dado['nome'], 'credito cliente': Valor_tranferencia, 'cod_parceiro': dado_parceiro['contrato'], 'parceiro': dado_parceiro['nome'],
                                'Credito parceiro': Valor_tranferencia}
                    extrato.append(operacao)
                    print(extrato)
                    print('Operação Realizada com sucesso!')
                    input('Pressione qualquer tecla para continuar...')
                    encontrou = "true"
            break
    if not 'encontrou' in locals():  # verificar se retornou algum parceiro para o usuário
        print('='*40)
        print("Parceiro não Cadastrado.....")
        print('='*40)

        input('Pressione qualquer tecla para continuar...')

        # else:
        #     resultado = 'não localizado'
        #     # print(f'Conta contrato {contrato} não localizada!')
        #     break

    cont = -1


def impressao_extrato(user):
    os.system('cls')
    msg.top()
    print('EXTRATO:')
    for dado in extrato:
        if dado['contrato'] == user:
            print(dado)
