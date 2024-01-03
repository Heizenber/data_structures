class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, successor, predecessor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class Empty(Exception):
    pass

if __name__ == '__main__':
    deque = _DoublyLinkedBase()
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