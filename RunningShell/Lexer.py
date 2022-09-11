import Position
import IllegalCharecterError
import Token
import Constants

class Lexer:
    def __init__(self, function, text):
        self.function = function
        self.text = text
        self.position = Position(-1, 0, -1, function, text)
        self.current_charecter = None
        self.advance()
    
    def advance(self):
        self.position.advance(self.current_charecter)
        self.current_charecter = self.text[self.position.idx] if self.position.index < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_charecter != None:
            if self.current_charecter in ' \t':
                self.advance()
            elif self.current_charecter in Constants:
                tokens.append(self.make_number())
            elif self.current_charecter == '+':
                tokens.append(Token(PLUS))
                self.advance()
            elif self.current_charecter == '-':
                tokens.append(Token(MINUS))
                self.advance()
            elif self.current_charecter == '*':
                tokens.append(Token(MUL))
                self.advance()
            elif self.current_charecter == '/':
                tokens.append(Token(DIV))
                self.advance()
            elif self.current_charecter == '(':
                tokens.append(Token(LPAREN))
                self.advance()
            elif self.current_charecter == ')':
                tokens.append(Token(RPAREN))
                self.advance()
            else:
                position_start = self.position.copy()
                char = self.current_charecter
                self.advance()
                return [], IllegalCharecterError(position_start, self.position, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_charecter != None and self.current_charecter in Constants + '.':
            if self.current_charecter == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_charecter
            self.advance()

        if dot_count == 0:
            return Token(INT, int(num_str))
        else:
            return Token(FLOAT, float(num_str))