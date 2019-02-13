import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS', 'LPAREN', 'RPAREN' ]

t_ignore = ' \t'
t_PLUS = r'\PLUS'
t_MINUS = r'\MIN'
t_TIMES = r'\TIM'
t_DIVIDE = r'\DIV'
t_EQUALS = r'\EQU'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NAME = r'^(!?(SUM)).'

lista = []

reserverd_words = ["PLUS", "MIN", "TIM", "DIV", "EQU"]
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
        if str(tok.value) in reserverd_words:
            tok.type = tok.value
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista

