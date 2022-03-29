import pytest
from hashtable import HashTable, BLANK

def test_should_create_table_default():
  assert HashTable() is not None

def test_should_create_table_fixed_size():
  assert HashTable(size=100) is not None

def test_should_report_size():
  assert len(HashTable(size=100)) == 100

def test_should_create_empty_values():
  # Given
  expected_values = [BLANK, BLANK, BLANK]
  hash_table = HashTable(size=3)

  # When
  actual_values = hash_table.values

  # Then
  assert actual_values == expected_values

def test_should_insert_key_value_pairs():
  # Given
  hash_table = HashTable(size=100)

  # When
  hash_table["hello"] = "hallo"
  hash_table[98.6] = 37
  hash_table[False] = True

  # Then
  assert "hallo" in hash_table.values
  assert 37 in hash_table.values
  assert True in hash_table.values

def test_should_not_change_size_when_insert_key_value_pairs():
  # Given
  hash_table = HashTable(size=100)

  # When
  hash_table[10] = 10

  # Then
  assert 10 in hash_table.values
  assert len(hash_table) == 100

def test_should_not_contain_none_values_when_created():
  assert None not in HashTable(size=100).values

def test_should_insert_none_value():
  hash_table = HashTable(size=100)
  hash_table['key'] = None
  assert None in hash_table.values

@pytest.fixture
def hash_table():
  sample_data = HashTable(size=100)
  sample_data['hola'] = 'hello'
  sample_data[98.6] = 37
  sample_data[False] = True
  return sample_data

def test_should_find_value_by_key(hash_table):
  assert hash_table['hola'] == 'hello'
  assert hash_table[98.6] == 37
  assert hash_table[False] is True

def test_should_find_key(hash_table):
  assert 'hola' in hash_table

def test_should_not_find_key(hash_table):
  assert 'missing_key' not in hash_table

def test_should_raise_error_on_missing_key(hash_table):
  with pytest.raises(KeyError) as exception_info:
    hash_table['missing_key']
  assert exception_info.value.args[0] == "missing_key"

def test_should_get_value(hash_table):
  assert hash_table




