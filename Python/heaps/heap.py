from unittest import TestCase, main

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return
        if self.heap[parent_idx] < self.heap[idx]:
            self.swap(parent_idx, idx)
            self.sift_up(parent_idx)
        
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_max(self):
        return self.heap[0] 

    def get_size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def extract_max(self):
        return self.remove(0)

    def sift_down(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        largest = idx  
        if left_idx < len(self.heap) and self.heap[left_idx] > self.heap[largest]:
            largest = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx] > self.heap[largest]:
            largest = right_idx
        if largest != idx:
            self.swap(largest, idx)
            self.sift_down(largest)

    def remove(self, idx):
        if len(self.heap) == 1:
            return self.heap.pop()
        if self.is_empty():
            return None 
        self.swap(idx, len(self.heap) - 1)
        value = self.heap.pop()
        self.sift_down(idx)
        return value

    def heapify(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.sift_down(i)

    def heap_sort(self, arr):
        self.heapify(arr)
        sorted_arr = []
        while not self.is_empty():
            sorted_arr.append(self.extract_max())
        return sorted_arr[::-1]










    
