﻿tokens = ('NUMBER','PLUS', 'MINUS', 'MUL', 'DIV', 'LPAR', 'RPAR', 'POW')
t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_MUL    = r'\*'
t_DIV    = r'/'
t_LPAR    = r'\('
t_RPAR    = r'\)'
t_POW    = r'\^'
def t_NUMBER(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t
t_ignore = " \t"
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
import ply.lex as lex;lex.lex()
def p_S(p):
  'S : E' # S → E
  print('S → E ', p[1])
def p_E_plus_T(p):
  'E : E PLUS T' # E → E + T
  p[0] = p[1] + p[3]
  print('E → E + T :', 'E: ',p[0], ' \t E1: ', p[1], '\t T: ', p[3])
def p_E_MINUS_T(p):
  'E : E MINUS T' # E → E - T
  p[0] = p[1] - p[3]
  print('E → E - T :', 'E: ',p[0], ' \t E1: ', p[1], '\t T: ', p[3])
def p_E_T(p):
  'E : T' # E → T
  p[0]=p[1]
  print('E → T :', p[1])
def p_T_MUL_F(p):
  'T : T MUL F' # T → T * F
  p[0] = p[1] * p[3]
  print('T → T * F :', 'T: ',p[0], ' \t T1: ', p[1], '\t F: ', p[3])
def p_T_DIV_F(p):
  'T : T DIV F' # T → T / F
  if p[3] != 0:  p[0] = p[1] / p[3]
  else: print('Error: Divide by zero '); p[0]=p[1]
  print('T → T / F :', 'T: ',p[0], ' \t T1: ', p[1], '\t F: ', p[3])
def p_T_F(p):
  'T : F' # T → F
  p[0]=p[1]
  print('T → F :', p[1])
def p_XP_POW_F(p):
  'F : XP POW F' # F → XP ^ F
  p[0] = pow(p[1], p[3])
  print('F → XP ^ F :', 'F: ',p[0], ' \t XP: ', p[1], '\t F1: ', p[3])
def p_F_XP(p):
  'F : XP' # F → X
  p[0]=p[1]
  print('F → XP :', p[1])
def p_XP_a(p):
  'XP : NUMBER' # XP → a
  p[0]=p[1]
  print('XP → a :', p[1])
def p_XP_lpar_E_rpar(p):
  'XP : LPAR E RPAR' # X → ( E )
  p[0]=p[2]
  print('XP → (E) :', p[0])
def p_error(p):
  print("Syntax error at '%s'" % p)
import ply.yacc as yacc; yacc.yacc()
while True:
  try:
    s = input('calc > ')
    if s.strip()=='':break
    yacc.parse(s)
  except: print('unexpected error')