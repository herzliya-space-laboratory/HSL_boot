
class RowNotExists(RuntimeError):
   def __init__(self, arg):
      self.args = arg

class SatelliteNotFound(RuntimeError):
   def __init__(self, arg):
      self.args = arg