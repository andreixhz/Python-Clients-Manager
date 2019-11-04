import json

class Cliente(object) :
    def __init__(self, id, nome='', idade=0, cupom='', cep=''):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cep = cep
        self.cupom = cupom

class ClientCrud() :
    def Criar(client):
        cList = []
        try :
            with open('cliente.data', 'r') as r :
                cList = json.load(r)
        except :
            print('Registrando pela primeira vez')
        with open('cliente.data', 'w') as f :
            cList.append(client)
            f.write(json.dumps(cList, default=convert_to_dict,indent=4))

    def GetAll(client):

        print('-' * 60)
        i = abs(4 - 18)
        print('Nome' + ' ' * i + 'Idade  Copum       Cep')
        print('-' * 60)

        with open('cliente.data', 'r') as r :
            cList = json.load(r, object_hook=dict_to_obj)
            for item in cList :
                print(item.nome + ' '*abs(len(item.nome) - 19) + item.idade + ' '*abs(len(item.cupom) - 8) + item.cupom + ' '*abs(len(item.cep) - 12) + item.cep)
            print('-' * 60)
            print('Numero total de Clientes: ' + str(len(cList)))
            print('-' * 60)

class Produto :
    def __init__(self, cod_bar='', fornecedor_id='', nome='', preco=''):
        self.cod_bar = cod_bar
        self.fornecedor_id = fornecedor_id
        self.nome = nome
        self.preco = preco

def convert_to_dict(obj):
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }
    obj_dict.update(obj.__dict__)
    return obj_dict

def dict_to_obj(our_dict):
    if "__class__" in our_dict:
        class_name = our_dict.pop("__class__")
        module_name = our_dict.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj


def CreateOrValidateData() :
    print('Iniciando Aplicação')
    print('Verificando clientes...')
    try:
         open('cliente.data', 'r')
    except IOError:
         open('cliente.data', 'a')

    print('Verificando Produtos...')
    try:
        open('Produto.data', 'r')
    except IOError:
        open('Produto.data', 'a')

    print('Validando Configurações')
    try:
        open('ini.data', 'r')
    except IOError:
        with open('ini.data', 'a') as s :
            s.write('0')
            s.write('\n0')

def Init() :
    while True:
        print('1 : Gerenciar')
        Operation = int(input())
        if (Operation == 1):
            Gerenciar()
        if(Operation ==  3):
            break

def Gerenciar() :
    while True :
        print('Gerenciar Clientes : 2 | Voltar : 5')
        Operation = int(input())
        if(Operation == 2) :
            GerenciarClientes()
        if(Operation == 5) :
            break

def GerenciarClientes() :
    while True :
        print('Criar : 1 | Mostrar : 2 | Voltar : 4')
        Operation = int(input())
        if(Operation == 4) :
            break
        if(Operation == 1) :
            GerenciarClientesCriar()
        if(Operation == 2) :
            ClientCrud.GetAll(Cliente)

def GerenciarClientesCriar() :
    cliente_nmr = input('Quantos clientes deseja cadastrar? : ')
    x = 0
    while x < int(cliente_nmr) :
        x=x+1
        nome = input('Nome : ')
        idade = input('Idade : ')
        cupom = input('Cupom : ')
        cep = input('Cep : ')
        with open("ini.data", 'r') as f:
            lines = f.readlines()
        with open('ini.data', 'w') as w :
            id = 1 + int(lines[0])
            w.writelines([str(id) + '\n' ,str(lines[1])])
            ClientCrud.Criar(Cliente(id, nome, idade, cupom, cep))



CreateOrValidateData()
Init()










