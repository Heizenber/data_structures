from heap import MaxHeap
from unittest import TestCase

class TestHeap(TestCase):
    def setUp(self):
        self.max_heap = MaxHeap()

    def test_insert(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(30)
        self.max_heap.insert(40)
        self.max_heap.insert(50)
        self.max_heap.insert(60)
        self.max_heap.insert(70)
        self.max_heap.insert(80)
        self.max_heap.insert(90)
        
        self.assertEqual(self.max_heap.heap, [90, 80, 60, 70, 30, 20, 50, 10, 40])

    def test_get_max(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(30)
        self.max_heap.insert(40)
        self.max_heap.insert(50)
        self.max_heap.insert(60)
        self.max_heap.insert(70)
        self.max_heap.insert(80)
        self.max_heap.insert(90)
        self.max_heap.insert(100)
        self.max_heap.insert(110)
        self.max_heap.insert(120)
        self.max_heap.insert(130)
        self.max_heap.insert(140)

        self.assertEqual(self.max_heap.get_max(), 140)

    def test_get_size(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(30)
        self.max_heap.insert(40)
        self.max_heap.insert(50)
        self.max_heap.insert(60)
        self.max_heap.insert(70)
        self.max_heap.insert(80)
        self.max_heap.insert(90)
        self.max_heap.insert(100)
        self.max_heap.insert(110)
        self.max_heap.insert(120)
        self.max_heap.insert(130)
        self.max_heap.insert(140)

        self.assertEqual(self.max_heap.get_size(), 14)

    def test_is_empty(self):
        self.assertTrue(self.max_heap.is_empty())

        self.max_heap.insert(10)
        self.assertFalse(self.max_heap.is_empty())

    def test_extract_max(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(30)
        self.max_heap.insert(40)
        self.max_heap.insert(50)
        self.max_heap.insert(60)
        self.max_heap.insert(70)
        self.max_heap.insert(80)
        self.max_heap.insert(90)
        self.max_heap.insert(100)
        self.max_heap.insert(110)
        self.max_heap.insert(120)
        self.max_heap.insert(130)
        self.max_heap.insert(140)

        self.assertEqual(self.max_heap.extract_max(), 140)
        self.assertEqual(self.max_heap.heap,  [130, 100, 120, 70, 90, 110, 50, 10, 40, 30, 80, 20, 60])


    def test_remove(self):
        self.max_heap.insert(10)
        self.max_heap.insert(20)
        self.max_heap.insert(30)
        self.max_heap.insert(40)
        self.max_heap.insert(50)
        self.max_heap.insert(60)
        self.max_heap.insert(70)
        self.max_heap.insert(80)
        self.max_heap.insert(90)
        
        

        self.max_heap.remove(0)
        self.assertEqual(self.max_heap.heap, [80, 70, 60, 40, 30, 20, 50, 10])

    def test_heapify(self):
        self.max_heap.heapify([10, 20, 30, 40, 50, 60, 70, 80, 90])
        self.assertEqual(self.max_heap.heap, [90, 80, 70, 40, 50, 60, 30, 20, 10])

    def test_heap_sort(self):
        self.assertEqual(self.max_heap.heap_sort([10, 20, 30, 40, 50, 60, 70, 80, 90]), [10, 20, 30, 40, 50, 60, 70, 80, 90])