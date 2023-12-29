class Vector:
    def __init__(self, capacity=16):
        self.array = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def size(self):
        return self.size 
    
    def capacity(self):
        return self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def at(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def push(self, item):
        if self.size == self.capacity:
            self.__resize()
        self.array.append(item)
        self.size += 1

    def __resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, index, item):
        if index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
           self.__resize()
        self.array.insert(index, item)
        self.size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.size == 0:
            raise IndexError("The array is empty")
        value = self.array.pop()
        self.size -= 1
        return value 
    
    def delete(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        self.array.pop(index)
        self.size -= 1

    def find(self, item):
        for i in range(self.size):
            if self.array[i] == item:
                return i 
        return -1

    



array = []
print(array.pop())




