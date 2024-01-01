def binary_search(array, target):
    min = 0
    max = len(array) - 1
    while min <= max:
        mid = (min + max) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
    return -1

def binary_search_recursion(array, target, min, max):
    if min > max:
        return -1
    mid = (min + max) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursion(array, target, mid + 1, max)
    else:
        return binary_search_recursion(array, target, min, mid - 1)

def test_binary_search():
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 1) == 0
    assert binary_search(array, 2) == 1
    assert binary_search(array, 3) == 2
    assert binary_search(array, 4) == 3
    assert binary_search(array, 5) == 4
    assert binary_search(array, 6) == -1


def test_binary_search_recursion():
    array = [1, 2, 3, 4, 5]
    assert binary_search_recursion(array, 1, 0, len(array) - 1) == 0
    assert binary_search_recursion(array, 2, 0, len(array) - 1) == 1
    assert binary_search_recursion(array, 3, 0, len(array) - 1) == 2
    assert binary_search_recursion(array, 4, 0, len(array) - 1) == 3
    assert binary_search_recursion(array, 5, 0, len(array) - 1) == 4
    assert binary_search_recursion(array, 6, 0, len(array) - 1) == -1

if __name__ == '__main__':
    test_binary_search()
    test_binary_search_recursion()
    print('All tests passed')