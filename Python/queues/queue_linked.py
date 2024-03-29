class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0
    
    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 
        self.length += 1

    def dequeue(self):
        if self.head is None:
            return None 
        if self.head == self.tail:
            value = self.head.value 
            self.head = None 
            self.tail = None 
        else:
            value = self.head.value 
            self.head = self.head.next 
        self.length -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            return None 
        return self.head.value
        
    
