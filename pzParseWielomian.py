# -----------------------------------------------------------------------------
# Parses a polynomial
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = [
            'TERM', 'NUMBER', 'DIV', 'MOD'
         ]

literals = ['+', '-', '*', '(', ')']

# Tokens

def t_TERM(t): # x or x5 or 3x6 or 0.5x8
    r'(\d+\.?\d*)?x\d*'
    pos_x = t.value.index('x')
    if pos_x == 0:
        xn_factor = 1
    else:
        xn_factor = float(t.value[:pos_x])
    if pos_x == len(t.value) - 1:
        n = 1
    else:
        n = int(t.value[pos_x + 1:])
    t.value = {n : xn_factor} # xn_factor * x^n
    return t


def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = {0 : float(t.value)} # float(t.value) * x^0
    return t

t_DIV = r'div'

t_MOD = r'mod'


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    raise ValueError

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
                ('left', '+', '-'),
                ('left', '*', 'DIV', 'MOD'),
                ('right', 'UMINUS'),
             )

from pzPolynomialOperations import *

def p_expression(p):
    '''expression : wielomian'''
    p[0] = p[1]
    print("Postać kanoniczna tego wielomianu: ", end='')
    print_poly(p[0])
        


def p_wielomian_binop(p):
    '''wielomian    : wielomian '+' wielomian
                    | wielomian '-' wielomian
                    | wielomian '*' wielomian
                    | wielomian DIV wielomian
                    | wielomian MOD wielomian
                    '''
    if p[2] == '+':
        p[0] = add_poly(p[1], p[3])
    elif p[2] == '-':
        p[0] = subt_poly(p[1], p[3])
    elif p[2] == '*':
        p[0] = multi_poly(p[1], p[3])
    elif p[2] == 'div':
        p[0] = div_poly(p[1], p[3])
    else: # p[2] == MOD
        p[0] = mod_poly(p[1], p[3])
     

def p_wielomian_uminus(p):     
    "wielomian : '-' wielomian %prec UMINUS"
    p[0] = negate_poly(p[2])


def p_wielomian_group(p):
    "wielomian : '(' wielomian ')'"
    p[0] = p[2]


def p_wielomian_term(p):
    "wielomian : TERM"
    p[0] = p[1]


def p_wielomian_number(p): 
    "wielomian : NUMBER"
    p[0] = p[1]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
    raise ValueError

import ply.yacc as yacc
yacc.yacc()

class Wielomian:
    def __init__(self):
        self = {}

def parse_wielomian(s):
    return yacc.parse(s)


##while 1:
##    try:
##        s = raw_input('Wprowadz wielomian > ')
##    except EOFError:
##        break
##    if not s:
##        continue
##    w = parse_wielomian(s)
##
##    try:
##        x = float(raw_input('Wprowadz x> '))
##    except EOFError:
##        break
##    if not s:
##        continue
##    w_x = calculate_poly(w, x)
##    print("Wartość wielomianu dla x =", x, "wynosi", w_x)
