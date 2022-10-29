import cadastros as cad
import funcao as fun
import mensagem as msg
import os
import mercado


def registro():
    os.system('cls')
    msg.top()
    print('\n\033[1m[~+] Area - Concessionária:\033[m\n')
    print('LEITURA DE DADOS DE CONSUMO E GERAÇÃO')
    contrato = fun.validaNumeroContrato()
    dado = fun.busca_cliente(contrato)
    if dado != -1:
        # for dado in cad.clientes:
        print('.'*40)
        print(dado)
        print('.'*40)
        consumido = fun.valida_consumo()  # validar consumo

        injetado = fun.valida_valor_injetado()
        # mercado.ganhando_credito(1,contrato,con)
        dado['consumido'].append(consumido)
        dado['injetado'].append(injetado)
        dado['saldo_energetico'] = injetado-consumido
        if injetado > consumido:
            credito = (injetado-consumido) * \
                cad.vCotacao[len(cad.vCotacao)-1]
            mercado.ganhando_credito(0, dado['contrato'], credito)
        print(
            f'Contrato: {dado["contrato"]} Nome: {dado["nome"]} Saldo: {dado["saldo_energetico"]} Crédito: R$ {dado["credito"]:.2f}')
        print('-'*80)

    else:
        print(f'Conta contrato: {contrato} não localizada!')

    input('Pressione  tecla ENTER para continuar...')
