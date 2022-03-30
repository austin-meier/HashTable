from typing import NamedTuple, Any

# https://realpython.com/python-hash-table/

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable():
  def __init__(self, size: int = 100):
    if size < 1:
      raise ValueError('The size must be a positive number')
    self._slots = size * [None]

  @classmethod
  def from_dict(cls, dictionary):
    hash_table = cls(size=len(dictionary) * 10)
    for key, value in dictionary.items():
      hash_table[key] = value
    return hash_table

  def __str__(self):
    pairs = []
    for key, value in self.pairs:
      pairs.append(f"{key!r}: {value!r}")
    return '{' + ", ".join(pairs) +  "}"

  def __len__(self):
    return len(self.pairs)

  def __setitem__(self, key, value):
    self._slots[self._index(key)] = Pair(key, value)

  def __getitem__(self, key):
    pair = self._slots[self._index(key)]
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
      self._slots[self._index(key)] = None
    else:
      raise KeyError(key)

  def __iter__(self):
    yield from self.keys

  def get(self, key, default=None):
    try:
      return self[key]
    except KeyError:
      return default

  @property
  def pairs(self):
    return {pair for pair in self._slots if pair}

  @property
  def values(self):
    # Already utilizes the conditional in the pairs property above
    return [pair.value for pair in self.pairs]

  @property
  def keys(self):
    return {pair.key for pair in self.pairs}

  @property
  def capacity(self):
    return len(self._slots)

  def _index(self, key):
    return hash(key) % self.capacity