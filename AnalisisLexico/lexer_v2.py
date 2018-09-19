import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'SUM'
t_MINUS = r'RES'
t_TIMES = r'\MUL'
t_DIVIDE = r'DIV'
t_EQUALS = r'EQU'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

lista = []
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    lista.append("'%s' -> Illegal character " % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#lex.input("x = 3 - 4 + 5 * 6")

def t_okens(expresion):
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista

