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
    print()
    vermelho = ('\033[1;41m  \033[m')
    verde = ('\033[1;42m  \033[m')
    injetado = [verde]*i
    injetadoInvert = []
    tamI = len(injetado)
    consumo = [vermelho]*c
    consumoInver = []
    tamC = len(consumo)
    if tamC < tamI:
        maior = tamI
        while tamC != 0:
            consumo.append('  ')
            tamC -= 1
        consumoInver = pilha_inversa(consumo)
        print('.'*50)
        for c in range(maior):
            print(f'        {consumoInver[c]}         {injetado[c]}')
        print('.'*50)
        print(f'Consumo:{vermelho} Injetado{verde}')
    elif tamC > tamI:
        maior = tamC
        while tamI != 0:
            injetado.append('  ')
            tamI -= 1
        injetadoInvert = pilha_inversa(injetado)
        print('.'*50)
        for c in range(maior):
            print(f'        {consumo[c]}         {injetadoInvert[c]}')
        print('.'*50)
        print(f'Consumo:{vermelho} Injetado{verde}')
