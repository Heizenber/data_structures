from basic_linked_list import _DoublyLinkedBase, Empty

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            return not (self == other)
        
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        if node is self._head or node is self._tail:
            return None
        return self.Position(self, node)
    
    def first(self):
        return self._make_position(self._head._next)

    def last(self):
        return self._make_position(self._tail._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._head, self._head._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._tail._prev, self._tail)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    
    def __repr__(self):
        return f'PositionalList({list(self)})'
    

if __name__ == '__main__':
    positional_list = PositionalList()
    print(positional_list)
    positional_list.add_first(1)
    print(positional_list)
    positional_list.add_last(2)
    print(positional_list)
    positional_list.add_first(3)
    print(positional_list)
    positional_list.add_last(4)
    print(positional_list)
    positional_list.delete(positional_list.first())
    print(positional_list)
    positional_list.delete(positional_list.last())
    print(positional_list)
    positional_list.delete(positional_list.first())
    print(positional_list)
    positional_list.delete(positional_list.last())
    print(positional_list)
    positional_list.add_first(1)
    print(positional_list)
    positional_list.add_last(2)
    print(positional_list)
    positional_list.add_first(3)
    print(positional_list)
    positional_list.add_last(4)
    print(positional_list)
    positional_list.replace(positional_list.first(), 5)
    print(positional_list)
    positional_list.replace(positional_list.last(), 6)
    print(positional_list)
    positional_list.replace(positional_list.first(), 7)
    print(positional_list)
    positional_list.replace(positional_list.last(), 8)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 9)
    print(positional_list)
    positional_list.add_after(positional_list.last(), 10)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 11)
    print(positional_list)
    positional_list.add_after(positional_list.last(), 12)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 13)
    print(positional_list)
    positional_list.add_after(positional_list.last(), 14)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 15)
    print(positional_list)
    positional_list.add_after(positional_list.last(), 16)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 17)
    print(positional_list)
    positional_list.add_after(positional_list.last(), 18)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 19)
    print(positional_list)
    positional_list.add_after(positional_list.last(), 20)
    print(positional_list)
    positional_list.add_before(positional_list.first(), 21)
    another_positional_list = PositionalList()
    another_positional_list.add_first(1)
    another_positional_list.add_last(2)
    positional_list.add_after(positional_list.last(), another_positional_list.first())
