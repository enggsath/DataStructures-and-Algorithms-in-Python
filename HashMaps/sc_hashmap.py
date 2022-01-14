from blossom_lib import flower_definitions
from linked_list import Node,LinkedList

class HashMap:
  def __init__(self,size):
    self.array_size=size
    self.array=[LinkedList() for i in range(self.array_size)]
  
  def hash(self,key):
    return sum(key.encode())

  def compressor(self,hash_code):
    return hash_code%self.array_size
  
  def assign(self,key,value):
    array_index=self.compressor(self.hash(key))
    pay_load=Node([key,value])
    list_at_array=self.array[array_index]
    for item in list_at_array:
      if(item[0]==key):
        item[1]=value
        return
    list_at_array.insert(pay_load)
    return

  def retrieve(self,key):
    array_index=self.compressor(self.hash(key))
    # pay_load=self.array[array_index]
    list_at_index=self.array[array_index]
    for item in list_at_index:
      if(item[0]==key):
        return item[1]
    return None

blossom=HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0],flower[1])
for fl in flower_definitions:
  print(f'key:{fl[0]} value:{blossom.retrieve(fl[0])}')