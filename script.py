class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value, '']
      return

    if current_array_value[0] == key or current_array_value[2] == 'X':
      self.array[array_index] = [key, value, '']
      return

    # Collision!

    number_collisions = 1
    new_array_index = -1

    while(current_array_value[0] != key) and new_array_index != array_index:
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value, '']
        return

      if current_array_value[0] == key or current_array_value[2] == 'X':
        self.array[new_array_index] = [key, value, '']
        return

      number_collisions += 1

    print('No more room!')
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      if possible_return_value[2] != 'X': 
        return possible_return_value[1]
      else:
        print('Nothing found')
        return None

    retrieval_collisions = 1
    retrieving_array_index = -1

    while (possible_return_value != key) and retrieving_array_index != array_index:
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        if possible_return_value[2] != 'X': 
          return possible_return_value[1]
        else:
          print('Nothing found')
          return None

      retrieval_collisions += 1

    print('Nothing found')
    return

  def remove(self, key):
    array_index = self.compressor(self.hash(key))
    posible_remove_value = self.array[array_index]

    if posible_remove_value is None:
      print("Nothing to remove")
      return None

    if posible_remove_value[0] == key:
      if posible_remove_value[2] != 'X':
        posible_remove_value[2] = 'X'
        return posible_remove_value[1]
      else:
        print("Nothing to remove")
        return None
    
    removing_collisions = 1
    removing_array_index = -1

    while (posible_remove_value != key) and array_index != removing_array_index:
      new_hash_code = self.hash(key, removing_collisions)
      removing_array_index = self.compressor(new_hash_code)
      posible_remove_value = self.array[removing_array_index]

      if posible_remove_value is None:
        print("Nothing to remove")
        return None

      if posible_remove_value[0] == key:
        if posible_remove_value[2] != 'X':
          posible_remove_value[2] = 'X'
          return posible_remove_value[1]
        else:
          print("Nothing to remove")
          return None

      removing_collisions += 1

    print("Nothing to remove")
    return
     



hash_map = HashMap(3)
hash_map.assign('gabbro','igneous')
hash_map.assign('sandstone','sedimentary')
hash_map.assign('gneiss','metamorphic')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
hash_map.remove('gneiss')
hash_map.retrieve('gneiss')
hash_map.assign('a','a1')
print(hash_map.array)
