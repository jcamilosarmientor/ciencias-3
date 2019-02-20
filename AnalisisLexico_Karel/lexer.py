import ply.lex as lex


declaracion = (
    'PROGRAMA',
        
)
expresion = (
    'IF',
    'ITERATE',
    'WHILE',
    'ENTONCES',
    'TURNOFF',
    'TURNLEFT',
    'MOVE',
    'PICKBEEPER',
    'PUTBEEPER',
    'RETURN',
    'EXPVACIA',
)

fbooleana=(
     'frontIsClear',
     'frontIsBlocked',
     'leftIsClear',
     'leftIsBlocked',
     'rightIsClear',
     'rightIsBlocked',
     'nextToABeeper',
     'notNextToABeeper',
     'anyBeepersInBeeperBag',
     'noBeepersInBeeperBag',
     'facingNorth',
     'facingSouth',
     'facingEast',
     'facingWest',
     'notFacingNorth',
     'notFacingSouth',
     'notFacingEast',
     'notFacingWest',
)

tokens =declaracion+expresion+fbooleana+('STARTARG','ENDARG','IDENTIFICADOR','TIPO','DECIMAL','ARGVACIO','TERMINO','CLAUSULAY','CLAUSULANO','ATOMICA','EQUALS','SEPARADOR','BLOQUEABIERTO','BLOQUECERRADO')

#t_if = r'if\('
t_ignore = ' \t'
t_STARTARG = r'\('
t_ENDARG = r'\)'
t_ARGVACIO = r'\(\)'
t_TERMINO=r'\|\|'
t_CLAUSULAY = r'&&'
t_CLAUSULANO = r'!'
t_TIPO=r'define' or r'void'
t_EQUALS = r'='
t_BLOQUEABIERTO =r'\{'
t_BLOQUECERRADO =r'\}'
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'

lista = []
def t_DECIMAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ITERATE(t):
    r'iterate'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_ENTONCES(t):
    r'entonces'
    return t

def t_IF(t):
    r'if'
    return t

def t_ATOMICA (t):
    r'iszero'
    return t

def t_TURNOFF (t):
    r'turnoff'
    return t

def t_TURNLEFT (t):
    r'turnleft'
    return t 

def t_MOVE (t):
    r'move'
    return t

def t_RETURN (t):
    r'return'
    return t

def t_PICKBEEPER (t):
    r'pickbeeper'
    return t

def t_EXPVACIA (t):
    r';'
    return t

def t_PROGRAMA(t):
    r'program'
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

