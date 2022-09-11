#All CSCode Tokens

INT				= 'INT'
FLOAT    	= 'FLOAT'
STRING			= 'STRING'
IDENTIFIER	= 'IDENTIFIER'
KEYWORD		= 'KEYWORD'
PLUS     	= 'PLUS'
MINUS    	= 'MINUS'
MUL      	= 'MUL'
DIV      	= 'DIV'
POW				= 'POW'
EQ					= 'EQ'
LPAREN   	= 'LPAREN'
RPAREN   	= 'RPAREN'

#Need to Add Keywords and Sort

class Token:
  def __init__ (self, type, value=None, position_start=None, position_end=None):
    self.type = type
    self.value = value

    if position_start:
      self.position_start = position_start.copy()
      self.position_end = position_start.copy()
      self.position_end.advance()

    if position_end:
      self.position_end = position_end.copy()

  def matches(self, type, value):
    return self.type == type and self.value == value

  def __repr__(self):
    if self.value: return f'{self.type}:{self.value}'
    return f'{self.type}'