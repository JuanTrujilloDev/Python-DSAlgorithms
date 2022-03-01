class MyArray:

    def __init__(self, *args):
        self.length = 0
        self.data = dict()
        if args:
            for value in args:
                self.data[self.length] = value
                self.length +=1

    def __str__(self):
        return str(self.data)
    
    def append(self, data):
        self.data[self.length] = data
        self.length += 1

    def get(self, index):
        if index not in self.data.keys():
            return IndexError('Index out of range')

        return self.data[index]

    def pop(self):
        data = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return data

    def delete(self, index):

        if index not in self.data.keys():
            return IndexError('Index out of range')

        data = self.data[index]
        self.shiftItems(index)
        del self.data[self.length-1]
        self.length -= 1
        return data
        
    
    def shiftItems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]




arr = MyArray(1,2,3)
arr.append(4)
print(arr.pop())
print(arr.delete(2))
print(arr)
print(arr.delete(1))
print(arr)
print(arr.length)


        