
from ast import Raise


class MyHash:
    
    
    def __init__(self, space=10):
        self.data = [None] * space
        
    
    def _hash(self, key):
        '''
        Funcion hash:
        
        Retorna un numero a partir de una serie de characteres
        Se pasa a ascii y se transforma a numero
        '''
        
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
            
        return hash
            
    def set(self, key, value):
        '''
        set() function.
        
        Recibe un par de key, value y utiliza la funcion de hash
        Para alocar el espacio del arreglo en el cual almacenar el valor
        
        '''
        if not self.data[self._hash(key)]:
            self.data[self._hash(key)] = [[key, value]]
            
        else:
            self.data[self._hash(key)].append([key,value])
        
        
    def get(self, key):
        '''
        get() Function
        
        Recibe una clave, esta la hashea a numero y busca en la posicion dentro del arreglo
        A partir de ese numero, al final retornara el valor en esa posicion
        '''
        if self.data[self._hash(key)]:
            
            if len(self.data[self._hash(key)]) == 1:
                return self.data[self._hash(key)][1]
            
            else:
                
                for array in self.data[self._hash(key)]:
                    if array[0] == key:
                        
                        return  array[1]
                    
        return KeyError('Key does not exist!')
    
    
    def keys(self):
        '''
        keys()
        
        Generates multiple keys for each key, value pair.
        '''
        
        for bucket in self.data:
            if bucket:
                if len(bucket) > 1 :
                    for array in bucket:
                        yield array[0]
                    
                    continue
                        
                yield bucket[0][0]
    

new_dict = MyHash(3)

new_dict.set('Nombre', 'Juan David')
new_dict.set('Edad', 23)
new_dict.set('Genero', 'Masculino')
new_dict.set('Cargo', 'Desarrollador Python')
new_dict.set('Mascotas', True)
print(new_dict.data)
print(new_dict.get('Nombre'))
print(new_dict.get('Edad'))

for i in new_dict.keys():
    print(i)
