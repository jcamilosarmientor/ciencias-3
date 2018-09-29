import ply.lex as lex


reservada = (

    # Palabras Reservadas
    'AVANZA',
    'APAGATE',
##    'GIRA-IZQUIERDA'
##    'COGE-ZUMBADOR'
##    'DEJA-ZUMBADOR'
    
)
condicion = (
    'SI',
    'SINO',
    'MIENTRAS',
    'ENTONCES',
)

##decisiones=(
##'frente-libre',
##'junto-a-zumbador',
##'frente-bloqueado',
##'no-junto-a-zumbador',
##'orientado-al-oeste',
##'izquierda-libre',
##'algun-zumbador-en-la-mochila',
##'no-orientado-al-norte',
##'izquierda-bloqueada',
##'ningun-zumbador-en-la-mochila',
##'no-orientado-al-sur',
##'derecha-libre',
##'orientado-al-norte',
##'no-orientado-al-este',
##'derecha-bloqueada',
##'orientado-al-sur',
##'no-orientado-al-oeste',
##)

tokens =reservada+condicion+('NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','SEPARADOR','GIRiZQ',)

t_ignore = ' \t'
t_PLUS = r'SUM'
t_MINUS = r'RES'
t_TIMES = r'MUL'
t_DIVIDE = r'DIV'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]'
t_SEPARADOR='-'
t_AVANZA='avanza'


lista = []
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SINO(t):
    r'sino'
    return t

def t_MIENTRAS(t):
    r'mientras'
    return t

def t_ENTONCES(t):
    r'entonces'
    return t

def t_SI(t):
    r'si'
    return t

# Error handling rule
def t_error(t):
    lista.append("'%s' -> Illegal character " % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#lex.input("x = 3 - 4 + 5 * 6")

def tokens(expresion):
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista

