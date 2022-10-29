import cadastros as cad
import funcao as fun
import mensagem as msg
import os


def cabecalho():
    concessionaria = ' <<<<  CONCESSIONÁRIA - MARANHÃO  >>>> '
    separador = '='*len(concessionaria)
    topo = separador + '\n' + concessionaria + '\n' + separador
    print(topo)
    # data_extenso()


cabecalho()

extrato_saida = []


def registro():
    os.system('cls')
    msg.top()

    x = 0
    print('LEITURA DE DADOS DE CONSUMO')

    contrato = fun.validaNumeroContrato()
    for dado in cad.gerador:
        if dado['contrato'] == contrato:
            print('.'*40)
            print(dado)
            print('.'*40)
            
            consumido = fun.valida_consumo() ##validar consumo
            #consumo = consumido
            #consumido += dado['consumido']
            injetado = fun.valida_valor_injetado()
            #injeta = injetado
            #injetado += dado['injetado']
            dado['consumido'] += consumido
            dado['injetado'] += injetado
            dado['saldo_energetico'] = dado['injetado']-dado['consumido']
            if injetado > consumido:
                dado['credito'] = dado['saldo_energetico'] * \
                    cad.gerador[1]['cotacao']
                operacao = {'contrato': dado['contrato'], 'cliente': dado['nome'],
                            'saldo energetico': dado['saldo_energetico'], 'credito': dado['credito']}
                extrato_saida.append(operacao)
            print(
                f'Contrato: {dado["contrato"]} Nome: {dado["nome"]} Saldo: {dado["saldo_energetico"]} Crédito: R$ {dado["credito"]:.2f}')
            print('-'*80)
            break
        else:
            x = x+1
            if x == len(cad.gerador):
                print(f'Conta contrato: {contrato}, não localizada!')
    # if resultado == 'não localizado':
    #     print(f'Conta contrato {contrato} não localizada!')

    input('Pressione  tecla ENTER para continuar...')
