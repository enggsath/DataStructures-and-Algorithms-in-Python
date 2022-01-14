class HashMap:
    def __init__(self,size): #creating underlying array for hashmap
        self.size = size
        self.array = [None for i in range(self.size)]

    def hash(self,key,number_collisions=0):     #creating a hash_function
        key_bytes =str(key).encode() #Turn the key into a list of bytes by calling str.encode() 
        hash_code = sum(key_bytes)+number_collisions #Turn the bytes object into a hash code by calling sum() on key_bytes
        return hash_code

    def compression(self,hash_code):#compress wide range of hash codes to digit with equivalent to array_indexes
        return hash_code%self.size

    #assign key to value using Open addressing collision
    def assign(self,key,value):
        array_index=self.compression(self.hash(key))
        current_value=self.array[array_index]
        # print(current_value)
        #if value at the indx is none,we assign key,value to that array_index
        #if the value @ index is occupied by and the old is equl to new key,we update it's value
        if(current_value==None or current_value[0]==key): 
            self.array[array_index]=[key,value]
            return
        number_collisions=1
        while(current_value[0]!=key):
            new_index=self.compression(self.hash(key,number_collisions))
            current_value=self.array[new_index]
            if(current_value==None or current_value[0]==key): 
                self.array[new_index]=[key,value]
                return
            else:
                number_collisions+=1
                if(number_collisions>self.size):
                    print(f"HashMap size exceeded,Unable to add {key}:{value}")
                    return

    def retrieve(self,key):
        array_index=self.compression(self.hash(key))
        current_value=self.array[array_index]
        if(current_value==None):
            return None
        elif(current_value[0]==key):
            return current_value[1]
        retrieval_collisions=1
        while(current_value[0]!=key):
            new_index=self.compression(self.hash(key,retrieval_collisions))
            current_value=self.array[new_index]
            if(current_value==None):
                return None
            elif(current_value[0]==key):
                return current_value[1]
            else:
                retrieval_collisions+=1
                if(retrieval_collisions>self.size):
                    print(f"Oops!\t you entered wrong key->{key},that is not assigned in hashMap")
                    return ""
    def __str__(self):
        st=''
        for k in self.array:
            pl=k[0]+' : '+k[1]
            st+=pl+'\n'
        return st

flower_definitions = [['begonia', 'cautiousness'], 
                      ['chrysanthemum', 'cheerfulness'],
                      ['carnation', 'memories'],
                      ['daisy', 'innocence'],
                      ['hyacinth', 'playfulness'],
                      ['lavender', 'devotion'], 
                      ['magnolia', 'dignity']]

blossom=HashMap(5)
for flower in flower_definitions:
    blossom.assign(flower[0],flower[1])
print(f'HashMap Blossom \n{blossom}')
for flower in flower_definitions:
    print(blossom.retrieve(flower[0]))
# print(blossom.retrieve('hyacinth'))
        
