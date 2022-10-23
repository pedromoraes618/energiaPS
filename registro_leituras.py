import cadastros as cad


def cabecalho():
    concessionaria = ' <<<<  CONCESSIONÁRIA - MARANHÃO  >>>> '
    separador = '='*len(concessionaria)
    topo = separador + '\n' + concessionaria + '\n' + separador
    print(topo)
    # data_extenso()


cabecalho()


def registro():
    x = 0
    print('REGISTRO DE DADOS ')

    contrato = int(input('Digite a Conta Contrado: '))
    for dado in cad.gerador:
        if dado['contrato'] == contrato:
            print('.'*40)
            print(dado)
            print('.'*40)
            consumido = int(input('Leitura de consumo(kw):'))
            consumido += dado['consumido']
            injetado = int(input('Leitura de valor injetado(kw):'))
            injetado += dado['injetado']
            dado['consumido'] = consumido
            dado['injetado'] = injetado
            dado['saldo_energetico'] = injetado-consumido
            if injetado > consumido:
                dado['credito'] = dado['saldo_energetico'] * \
                    cad.gerador[1]['cotacao']
            print('Contrato: ', dado['contrato'], 'Nome: ',
                  dado['nome'], 'Crédito: E$', dado['credito'])
            print('-'*80)
            break
        else:
            x = x+1
            if x == len(cad.gerador):
                print(f'Conta contrato: {contrato}, não localizada!')
    # if resultado == 'não localizado':
    #     print(f'Conta contrato {contrato} não localizada!')

    input('Pressione qualquer tecla para continuar...')
