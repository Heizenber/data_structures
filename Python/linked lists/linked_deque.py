from basic_linked_list import _DoublyLinkedBase

class Empty(Exception):
    pass

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._head._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._tail._prev._element
    
    def insert_first(self, e):
        self._insert_between(e, self._head, self._head._next)

    def insert_last(self, e):
        self._insert_between(e, self._tail._prev, self._tail)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._head._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._tail._prev)
    
    def __str__(self):
        if self.is_empty():
            return 'Deque is empty'
        s = ['Deque: ']
        walk = self._head._next
        while walk is not self._tail:
            s.append(f'{walk._element} ')
            walk = walk._next
        return ''.join(s)
    


if __name__ == '__main__':
    deque = LinkedDeque()
    print(deque)
    deque.insert_first(1)
    print(deque)
    deque.insert_last(2)
    print(deque)
    deque.insert_first(3)
    print(deque)
    deque.insert_last(4)
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.insert_first(5)
    print(deque)
    deque.insert_last(6)
    print(deque)
    deque.insert_first(7)
    print(deque)
    deque.insert_last(8)
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.insert_first(9)
    print(deque)
    deque.insert_last(10)
    print(deque)
    deque.insert_first(11)
    print(deque)
    deque.insert_last(12)
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.insert_first(13)
    print(deque)
    deque.insert_last(14)
    print(deque)
    deque.insert_first(15)
    print(deque)
    deque.insert_last(16)
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.insert_first(17)
    print(deque)
    deque.insert_last(18)
    print(deque)
    deque.insert_first(19)
    print(deque)
    deque.insert_last(20)
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.delete_first()
    print(deque)
    deque.delete_last()
    print(deque)
    deque.insert_first(21)
    print(deque)
    deque.insert_last(22)
    print(deque)
    deque.insert_first(23)
    print(deque)
    deque.insert_last(24)
    print(deque)