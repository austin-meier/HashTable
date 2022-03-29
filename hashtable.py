# https://realpython.com/python-hash-table/
# Default value placeholder/sentinel value
BLANK = object()

class HashTable():
  def __init__(self, size = 100):
    self.values = size * [BLANK]

  def __len__(self):
    return len(self.values)

  def __setitem__(self, key, value):
    index = hash(key) % len(self)
    self.values[index] = value

  def __getitem__(self, key):
    index = hash(key) % len(self)
    value = self.values[index]
    if value is BLANK:
      raise KeyError(key)
    return value

  def __contains__(self, key):
    try:
      self[key]
    except KeyError:
      return False
    else:
      return True