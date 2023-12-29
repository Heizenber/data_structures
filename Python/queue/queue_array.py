class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.length = 0
        self.queue = [None] * capacity

    def empty(self):
        return self.length == 0

    def enqueue(self, value):
        if self.length == self.capacity:
            raise Exception("Queue is full")
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.length += 1

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.length -= 1
        return value

    def peek(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def __str__(self) -> str:
        return str(self.queue)