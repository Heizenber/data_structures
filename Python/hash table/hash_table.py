class HashTable:
    def __init__(self, size):
        self.values = [None] * size
        self.keys = [None] * size
        self.size = size
        self.length = 0

    def hash(self, key):
        return hash(key) % self.size
    
    def _linear_probing(self, index):
        return (index + 1) % self.size
    
    def add(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._linear_probing(index)
        self.keys[index] = key
        self.values[index] = value
        self.length += 1

    def exists(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = self._linear_probing(index)
        return False
    
    def get(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probing(index)
        return None
    
    def remove(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.length -= 1
                return
            index = self._linear_probing(index)

