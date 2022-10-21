import cadastros as cad


def cabecalho():
    concessionaria = ' <<<<  CONCESSIONÁRIA - MARANHÃO  >>>> '
    separador = '='*len(concessionaria)
    topo = separador + '\n' + concessionaria + '\n' + separador
    print(topo)
    #data_extenso()


cabecalho()


def registro():
    print('REGISTRO DE DADOS ')
    cont = -1

    contrato = str(input('Digite a Conta Contrado: '))
    for dado in cad.gerador:
        cont = cont+1
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
            dado['credito'] = dado['saldo_energetico'] * dado['conversor']
            break
    # if resultado == 'não localizado':
    #     print(f'Conta contrato {contrato} não localizada!')
    print('Contrato: ', dado['contrato'], 'Nome: ',
          dado['nome'], 'Crédito: E$', dado['credito'])
    print('-'*80)
    input('Pressione qualquer tecla para continuar...')
    cont = -1
