import ply.yacc as yacc
from recursivodesc_lex import tokens

def p_expr_plus_term(p):
    'Expr : Expr PLUS Term'
    p[0] = p[1] + p[3]

def p_expr_minus_term(p):
    'Expr : Expr MINUS Term'
    p[0] = p[1] - p[3]

def p_expr_term(p):
    'Expr : Term'
    p[0] = p[1]


def p_term_times_factor(p):
    'Term : Term TIMES Factor'
    p[0] = p[1] * p[3]

def p_term_divide_factor(p):
    'Term : Term DIVIDE Factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'Term : Factor'
    p[0] = p[1]


def p_factor_number(p):
    'Factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'Factor : LPAREN Expr RPAREN'
    p[0] = p[2]


def p_error(p):
    print(f'Erro na expressão: {p.value}')


parser = yacc.yacc()

parsedString = input()

resultado = parser.parse(parsedString)

print(f'{resultado}')