import cadastros as cad


def mercado():
    print('MERCADO DE CRÉDITOS ')
    cont = -1
    repetir = 's'
    # tempDado.clear()
    # while repetir == 's':
    # dado.clear()
    contrato = int(input('Digite a Conta Contrado: '))
    for dado in cad.gerador:
        cont = cont+1

        if dado['contrato'] == contrato:
            print('.'*40)
            print(dado)
            print('.'*40)
            uso = int(input('Valor da saida de crédito: E$'))
            dado['credito'] -= uso
            break
            # else:
            #     resultado = 'não localizado'
            #     # print(f'Conta contrato {contrato} não localizada!')
            #     break
    print('Contrato: ', dado['contrato'], 'Nome: ',
          dado['nome'], 'Crédito: E$', dado['credito'])
    print('-'*80)
    input('Pressione qualquer tecla para continuar...')
    cont = -1
