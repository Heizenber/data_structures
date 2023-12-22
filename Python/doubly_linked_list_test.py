import pytest
from double_linked_list import LinkedList  # assuming your class is named LinkedList

def setup_function():
    global list
    list = LinkedList()

def test_empty():
    assert list.empty() == True

def test_insert():
    list.insert(0, 5)
    assert list.length == 1
    assert list.head.value == 5
    assert list.tail.value == 5

def test_remove_value():
    list.insert(0, 5)
    list.insert(1, 10)
    list.remove_value(5)
    assert list.length == 1
    assert list.head.value == 10
    assert list.tail.value == 10

def test_reverse():
    list.insert(0, 5)
    list.insert(1, 10)
    list.reverse()
    assert list.head.value == 10
    assert list.tail.value == 5

def test_value_n_from_end():
    list.insert(0, 5)
    list.insert(1, 10)
    list.insert(2, 15)
    assert list.value_n_from_end(1) == 10

def test_iter():
    list.insert(0, 5)
    list.insert(1, 10)
    values = [value for value in list]
    assert values == [5, 10]

def test_pop_front():
    list.insert(0, 5)
    list.insert(1, 10)
    list.pop_front()
    assert list.head.value == 10
    assert list.tail.value == 10

def test_pop_back():
    list.insert(0, 5)
    list.insert(1, 10)
    list.pop_back()
    assert list.head.value == 5
    assert list.tail.value == 5

def test_front():
    list.insert(0, 5)
    list.insert(1, 10)
    assert list.front() == 5

def test_back():
    list.insert(0, 5)
    list.insert(1, 10)
    assert list.back() == 10

def test_push_front():
    list.push_front(5)
    assert list.head.value == 5
    assert list.tail.value == 5

def test_push_back():
    list.push_back(5)
    assert list.head.value == 5
    assert list.tail.value == 5

def test_pop_front():
    list.push_front(5)
    list.push_front(10)
    list.pop_front()
    assert list.head.value == 5
    assert list.tail.value == 5

def test_pop_back():
    list.push_front(5)
    list.push_front(10)
    list.pop_back()
    assert list.head.value == 10
    assert list.tail.value == 10

def test_front():
    list.push_front(5)
    list.push_front(10)
    assert list.front() == 10

def test_back():
    list.push_front(5)
    list.push_front(10)
    assert list.back() == 5

