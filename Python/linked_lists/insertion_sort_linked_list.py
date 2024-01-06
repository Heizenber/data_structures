from positional_linked_list import PositionalList

def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot) 
                L.add_before(walk, value)


if __name__ == '__main__':
    linked_list = PositionalList()
    linked_list.add_first(1)
    linked_list.add_last(3)
    linked_list.add_last(2)
    linked_list.add_last(5)
    linked_list.add_last(4)
    print("Before sorting:")
    for node in linked_list:
        print(node)
    insertion_sort(linked_list)
    print("After sorting:")
    for node in linked_list:
        print(node)
