from typing import NamedTuple, Any

# https://realpython.com/python-hash-table/
# Default value placeholder/sentinel value

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable():
  def __init__(self, size = 100):
    self._pairs = size * [None]

  def __len__(self):
    return len(self._pairs)

  def __setitem__(self, key, value):
    self._pairs[self._index(key)] = Pair(key, value)

  def __getitem__(self, key):
    pair = self._pairs[self._index(key)]
    if pair is None:
      raise KeyError(key)
    return pair.value

  def __contains__(self, key):
    try:
      self[key]
    except KeyError:
      return False
    else:
      return True

  def __delitem__(self, key):
    if key in self:
      self._pairs[self._index(key)] = None
    else:
      raise KeyError(key)

  def get(self, key, default=None):
    try:
      return self[key]
    except KeyError:
      return default

  @property
  def pairs(self):
    return {pair for pair in self._pairs if pair}

  @property
  def values(self):
    # Already utilizes the conditional in the pairs property above
    return [pair.value for pair in self.pairs]

  @property
  def keys(self):
    return {pair.key for pair in self.pairs}

  def _index(self, key):
    return hash(key) % len(self)