# methods:
#     init for Node and for DoublyLinkedBase
#     len
#     is_empty
#     _insert_between
#     _delete_node
#     make class Empty




class _DoublyLinkedBase:
    class Node:
        __slots__ = '_element', '_next', '_prev'
        def __init__(self, element, next, prev):
            self._element = element 
            self._next = next 
            self._prev = prev 

    def __init__(self):
        self._head = self.Node(None, None, None)
        self._tail = self.Node(None, None, None)
        self._head.next = self._tail 
        self._tail.prev = self._head 
        self._size = 0 


    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0 

    def _insert_between(self, e, predecessor, successor):
        newNode = Node(e, successor, predecessor)
        predecessor._next = newNode
        successor._prev = newNode
        self._size += 1
        return newNode 

    def _delete_node(self, node):
        successor = node.next 
        predecessor = node.prev 
        successor._prev = predecessor
        predecessor._next = successor
        self._size -= 1
        element = node._element
        node._element = node._next = node._prev = None 
        return element

class Empty(Exception):
    pass 



