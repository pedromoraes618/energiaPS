import os
from datetime import date, time
meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio",
             "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


def data_extenso():
    hoje = date.today()

    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    mes = meses[mes]
    print(f'São Luís, {dia} de  {mes} de {ano}.')


def sobre():
    os.system('cls')
    print('''
SEMINÁRIO TEMÁTICO 3.
Componentes:
Ana Paula;
Clauberth Pinho;
Marcelo Carvalho;
Mateus Vaz;
Pedro Henrique;
Paulo Vinicius
Tatiana Barbosa;

O PROJETO:
PARTICIPANTES DO PROJETO:
Concessionária elétrica (EQUATORIAL)
Comercio – Comércios cadastrados (farmácias, supermercados, etc…)
Caridade – Instituições de caridade cadastradas.
Geradores – Clientes da concessionária que possui geração própria de energia via placas solares.

GERAÇÃO DOS CRÉDITOS:
Os créditos terão origem através da geração de energia realizada pelos geradores.
Exemplo: Num mês um gerador que tenha gerado mais energia do que usa, terá um saldo de reserva, 
o gerador poderá determinar um percentual deste saldo que será transformado em credito elétrico (E$)

UTILIZAÇÃO DOS CRÉDITOS:
Doação para instituições de caridade.
Pagamento de compras num supermercado, farmácia, etc…

OBJETIVOS DO SSITEMA:
Incentivar o uso de energia limpa, placas solares, 
oferecendo vantagens além da preservação da natureza.
O consumidores/geradores podem utilizar os saldos excedentes de suas gerações 
para compra de produtos ou serviços, gerando assim economia e circulação de bens e serviços.

    ''')

    input('Pressione qualquer tecla para continuar...')


def top():
    nome = 'SYSTEMA: ENERGIA POSITIVA'
    print('~='*50)
    print(f'{nome:^100}')
    print('~='*50)
    data_extenso()


# def apresentacao():
#     print('''
#         Esse aprojeto visa apresentar uma proposta de incentivo ao uso da energia solar, oferencendo crédito para os consumidores com geração excedente
#     esse credito poderá ser utilizado como moeda de troca, mercadoriasou serviços, e como doação à instiuições de caridade cadastradas.
#     Com isso, o sistema energetico do Brasil ganha com mais geração diminuindo assim o uso de termo eletricas.        
#     ''')

