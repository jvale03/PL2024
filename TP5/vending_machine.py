import sys
import re
import ply.lex as lex 

stock = []
saldo = 0

tokens = ('LISTAR','SELECIONAR','SAIR','MOEDA')
t_LISTAR = r'LISTAR'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_MOEDA = r'MOEDA'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

def t_ignore(t):
    r' \t\n'

def fill_stock(name_file):
    file = open(name_file, "r")
    for line in file:
        integers = re.findall(r'\d+', line)
        string = re.findall(r'[a-zA-Z]+', line)
        floats = re.findall(r'\d+\.\d+', line)
        dict = {"cod" : int(integers[0]), "nome" : string[0], "quant" : int(integers[1]), "preco" : float(floats[0])}
        stock.append(dict)
    file.close()
    return 0

def listar():
    for item in stock:
        print(f"{item['cod']} | {item['nome']} | {item['quant']} | {item['preco']}")
    return 0

def inserir(valor):
    global saldo
    saldo += valor

def selecionar(cod):
    global saldo
    for item in stock:
        if item['cod'] == cod and item['quant'] > 0:
            if item['preco'] > saldo:
                return "Saldo insuficiente!"
            else:
                item['quant'] -= 1
                saldo -= item['preco']
                saldo = round(saldo, 2)
                return f"Pode retirar o seu produto! {item['nome']}"
    return "Produto indisponível!"

def sair():
    global saldo
    return f"Retire o seu saldo {saldo}!"
    

if __name__ == "__main__":
    fill_stock(sys.argv[1])
    inserir(1)
    listar()
    print(selecionar(1))
    print(sair())