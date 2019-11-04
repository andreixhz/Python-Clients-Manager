class Cliente:

    def __init__(self, nome, cupom, idade):
        self.nome = nome
        self.cupom = cupom
        self.idade = idade


def Cls() :
    print("\n" * 100)

Clientes = []

def OperarCriar(NClientes):
    x = 0
    while x < NClientes:
        print('#{}'.format(x))
        nome = input('Qual nome do cliente? :')
        idade = input('Idade: ')
        cupom = input('cupom? s/n :')
        Clientes.append(Cliente(nome, cupom,idade))
        x = x + 1
    print('Você cadastrou {} clientes :)'.format(NClientes))

def OperarVizualizarClientes():
    print('-'*40)
    i = abs(4 - 18)
    print('Nome'+ ' '*i +'Idade' + '   Tem cupom')
    print('-'*40)
    for x in Clientes:
        i = abs(len(x.nome) - 18)
        print('{} {} {} {} {}'.format(x.nome, ' '*i, x.idade, ' '*7, x.cupom))
    print('-'*40)


def Operar():
    while True :
        print('1: Criar Cliente | 2: Ver Clientes | 5: Voltar')
        Operation1 = input()
        if int(Operation1) == 1 :
            nrmClientes = int(input('Quantos clientes deseja Adcionar? :'))
            OperarCriar(nrmClientes)
        if int(Operation1) == 2 :
            OperarVizualizarClientes()
        if int(Operation1) == 5 :
            break;

while True :
    print('1: Operar | 5: sair')
    Operation = input();
    if int(Operation) == 1 :
        Cls()
        Operar()
    if int(Operation) == 5 :
        break;





