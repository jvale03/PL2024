import sys
import re
import ply.lex as lex 

stock = []
saldo = 0

tokens = ('LISTAR','SELECIONAR','SAIR','MOEDA','COD','CASH')
t_LISTAR = r'LISTAR'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_MOEDA = r'MOEDA'
t_COD = r'\d+'
t_CASH = r'\d+[ec]?'
t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

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
    return f"Retire o seu saldo: {convert_coins(saldo)}!"

def coins_convert(array):
    number = 0
    for i in range(len(array)):
        if array[i].value[-1] == "e":
            number += float(array[i].value[:-1])
        elif array[i].value[1] == "c":
            number += float(f"0.0{array[i].value[:-1]}")
        else:
            number += float(f"0.{array[i].value[:-1]}")
    return round(number,2)

def convert_coins(valor):
    # valor = float(value)  # Converte o saldo para um número decimal
    moedas = {'2€': 0, '1€': 0, '50c': 0, '20c': 0, '10c': 0,'5c': 0, '2c': 0, '1c': 0}  # Dicionário para armazenar a quantidade de cada moeda

    # Converte o valor para a quantidade de moedas necessárias
    while valor >= 2:
        moedas['2€'] += 1
        valor -= 2
    while valor >= 1:
        moedas['1€'] += 1
        valor -= 1
    while valor >= 0.5:
        moedas['50c'] += 1
        valor -= 0.5
    while valor >= 0.2:
        moedas['20c'] += 1
        valor -= 0.2
    while valor >= 0.1:
        moedas['10c'] += 1
        valor -= 0.1
    while valor >= 0.05:
        moedas['5c'] += 1
        valor -= 0.05
    while valor >= 0.02:
        moedas['2c'] += 1
        valor -= 0.02
    while valor >= 0.01:
        moedas['1c'] += 1
        valor -= 0.01

    # Formata e exibe o resultado
    resultado = [f'{quantidade}x {moeda}' for moeda, quantidade in moedas.items() if quantidade > 0]
    return resultado
    
def start_system():
    global saldo
    lexer = lex.lex()
    tokens_array = []
    while True:
        tokens_array.clear()
        data = input()
        lexer.input(data)
        tok = lexer.token()
        while tok:
            tokens_array.append(tok)
            tok = lexer.token()
        if tokens_array[0].type == "MOEDA":
            inserir(coins_convert(tokens_array[1:]))
            print(f"Saldo: {saldo}")
        elif tokens_array[0].type == "LISTAR":
            listar()
            print(f"Saldo: {saldo}")
        elif tokens_array[0].type == "SELECIONAR":
            print(selecionar(int(tokens_array[1].value)))
            print(f"Saldo: {saldo}")
        elif tokens_array[0].type == "SAIR":
            print(sair())
            break
    return 0

if __name__ == "__main__":
    fill_stock(sys.argv[1])
    start_system()
