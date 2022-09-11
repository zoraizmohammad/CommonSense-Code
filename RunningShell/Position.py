class Position:
    def __init__(self, index, line, collumn, function, functiontext):
        self.index = index
        self.line = line
        self.collumn = collumn
        self.function = function
        self.functiontext = functiontext

    def advance(self, current_char):
        self.index += 1
        self.collumn += 1

        if current_char == '\n':
            self.line += 1
            self.collumn = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.collumnlumn, self.function, self.functiontext)