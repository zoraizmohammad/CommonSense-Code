class Error:
  def __init__(self, start, end, name, details):
    self.start = start
    self.end = end
    self.error = error
    self.details = details
    
class IllegalCharError(Error):
  def __init__(self, start, end, details):
    super().__init__(start, end, 'Illegal Character', details)

class ExpectedCharError(Error):
  def __init__(self, start, end, details):
    super().__init__(start, end, 'Expected Character', details)
