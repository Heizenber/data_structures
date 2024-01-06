from positional_linked_list import PositionalList

class FavoritesList:
    class _Item:
        __slots__ = '_value', '_count'
        
        def __init__(self, e):
            self._value = e
            self._count = 0

    def __init__(self):
        self._data = PositionalList() # list of _Item instances

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    # nonpublic utilities
    def _find_position(self, e):
        walk = self._data.first()
        # why do we use walk.element()._element instead of walk.element()?
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        # Move item at Position p earlier in the list based on access count
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))


    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)



if __name__ == '__main__':
    favorites = FavoritesList()
    
    favorites._data.add_first(favorites._Item(1))
    favorites._data.add_first(favorites._Item(2))
    favorites._data.add_first(favorites._Item(3))
    favorites._data.add_first(favorites._Item(2))
    favorites._data.add_first(favorites._Item(8))
    favorites._data.add_first(favorites._Item(7))
    favorites.access(2)

