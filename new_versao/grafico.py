import os
import mensagem as msg
import cadastros as cad


def grafico_cliente(user):
    os.system('cls')
    msg.top()
    print('\nGráfico de Clientes Geradores\n')
    for dado in cad.gerador:
        if dado['contrato'] == user:
            print('Contrato: ', dado['contrato'], 'Nome: ',
                  dado['nome'], ' Crédito:', dado['credito'])
            consC = (dado["consumido"])//100
            consI = (dado["injetado"])//100
            grafico_vertical(consI, consC)
            print(
                f'{"Energ. Consumida:":20} \033[1;41m{dado["consumido"]}\033[m', end=' ')
            print(
                f'{"Energ. Injetada:":20} \033[1;42m{dado["injetado"]}\033[m')
            # print(
            #     f'{"Consumo:":9} \033[1;41m{dado["consumido"]}\033[m')
            # print(
            #     f'{"Injetado:":9} \033[1;42m{dado["injetado"]}\033[m')

    input('Pressione  tecla ENTER para voltar...')


def push(s, elemento):
    s.append(elemento)
    # copia.append(elemento)


def pilha_inversa(s):
    pilha_inv = []
    while not isempty(s):
        push(pilha_inv, pop(s))

    return pilha_inv


def pop(s):
    if not isempty(s):
        return s.pop()


def isempty(s):
    return len(s) == 0


def grafico_vertical(i, c):
    vermelho = ('\033[1;41m  \033[m')
    verde = ('\033[1;42m  \033[m')
    injetado = [verde]*i
    injetadoInvert = []
    tamI = len(injetado)
    consumo = [vermelho]*c
    consumoInver = []
    tamC = len(consumo)
    if tamC < tamI:
        dif = tamI-tamC
        maior = tamI
        while dif != 0:
            consumo.append('  ')
            dif -= 1
        consumoInver = pilha_inversa(consumo)
        print('.'*55)
        for c in range(maior):
            print(
                f'{"|":>22}{consumoInver[c]}{"|"}{"|":>22}{injetado[c]}{"|"}')
        print('.'*55)
        #print(f'Consumo:{vermelho} Injetado{verde}')
    elif tamC > tamI:
        dif = tamC-tamI
        maior = tamC
        while dif != 0:
            injetado.append('  ')
            tamI -= 1
        injetadoInvert = pilha_inversa(injetado)
        print('.'*55)
        for c in range(maior):
            print(f'|   {consumo[c]}   |   {injetadoInvert[c]}   |')
        print('.'*55)
        #print(f'Consumo:{vermelho} Injetado{verde}')


def grafico_horizontal(contrato):
    for dado in cad.gerador:
        if dado['contrato'] == contrato:
            # print('Contrato: ', dado['contrato'], 'Nome: ',
            #      dado['nome'], ' Crédito:', dado['credito'])
            print(f'{"Energ. Consumida:":20} {dado["consumido"]:<5}', end=' ')
            cons = (dado["consumido"])//100
            print('\033[1;41m \033[m'*cons)
            print(f'{"Energ. Injetada:":20} {dado["injetado"]:<5}', end=' ')
            cons = (dado["injetado"])//100
            print('\033[1;42m \033[m'*cons)
            print('-'*100)
