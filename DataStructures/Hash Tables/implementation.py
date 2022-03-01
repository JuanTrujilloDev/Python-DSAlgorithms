
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
        
        self.data[self._hash(key)] = [key, value]
        
        
    def get(self, key):
        '''
        get() Function
        
        Recibe una clave, esta la hashea a numero y busca en la posicion dentro del arreglo
        A partir de ese numero, al final retornara el valor en esa posicion
        '''
        
        return self.data[self._hash(key)][1]
    
    

new_dict = MyHash(50)

new_dict.set('Nombre', 'Juan David')
new_dict.set('Edad', 23)
print(new_dict.get('Nombre'))
print(new_dict.get('Edad'))