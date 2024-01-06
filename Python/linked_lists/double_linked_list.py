class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, target):
        current = self.head 
        while current:
            if current.value == target:
                return current 
            current = current.next 
        return None 
    
    def size(self):
        return self.length
    
    def empty(self):
        return self.length == 0
    
    def value_at(self, index):
        if index >= self.length or index < 0:
            return None
        current = self.head 
        for _ in range(index):
            current = current.next 
        return current.value
    
    
    def push_front(self, value):
        node = Node(value)
        if self.empty():
            self.head = node 
            self.tail = node 
        else:
            node.next = self.head 
            self.head.prev = node 
            self.head = node 
        self.length += 1

    def pop_front(self):
        if self.empty():
            return None 
        if self.length == 1:
            value = self.head.value 
            self.head = None 
            self.tail = None 
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return value
    
    def push_back(self, value):
        node = Node(value)
        if self.empty():
            self.head = node 
            self.tail = node 
        else:
            node.prev = self.tail 
            self.tail.next = node 
            self.tail = node 
        self.length += 1

    def pop_back(self):
        if self.empty():
            return None 
        if self.length == 1:
            value = self.head.value 
            self.head = None 
            self.tail = None 
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return value
    
    
    def front(self):
        if self.empty():
            return None 
        return self.head.value
    
    def back(self):
        if self.empty():
            return None 
        return self.tail.value
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.push_front(value)
        elif index == self.length:
            self.push_back(value)
        else:
            node = Node(value)
            current = self.head
            for _ in range(index):
                current = current.next
            node.next = current
            node.prev = current.prev
            current.prev.next = node
            current.prev = node
            self.length += 1

    def erase(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_front()
        elif index == self.length - 1:
            self.pop_back()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.length -= 1

    def value_n_from_end(self, n):
        if n < 0 or n >= self.length:
            return None 
        if n == self.length - 1:
            return self.front()
        else:
            current = self.tail 
            for _ in range(n):
                current = current.prev 
            return current.value

    def reverse(self):
        if self.empty():
            return None 
        current = self.head 
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def remove_value(self, value):
        if self.empty():
            return None
        current = self.head 
        for i in range(self.length):
            if current.value == value:
                if current == self.head:
                    self.pop_front()
                elif current == self.tail:  
                    self.pop_back()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.length -= 1
                return 
        return None

        
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    

    
    