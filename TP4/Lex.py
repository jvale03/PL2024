import ply.lex as lex
import sys


tokens = ('NUMBER','ID','SELECT','FROM','WHERE','COMPARE','COMMA')

reserved_keywords = {
    'FROM': 'FROM',
    'SELECT': 'SELECT',
    'WHERE': 'WHERE'
    }

t_COMMA = r','
t_COMPARE = r'>=|<=|>|<|='

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved_keywords.get(t.value.upper(), 'ID')
    return t

def t_NUMBER(t):
    r'[-+]?\d+(\.\d+)?'
    t.value = int(t.value) if t.value.find('.') == -1 else float(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(sys.argv[1])

tok = lexer.token()

while tok != None:
    print(tok)
    tok = lexer.token()