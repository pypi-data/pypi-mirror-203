from .Heap import Heap

class MaxHeap(Heap):
    def insert(self, key: int):
        # Inserts the value key to the elements list and maintains heap properties.
        self.elements.append(key)
        self.heapifyUp(len(self.elements) - 1)

    def delete(self, key: int):
        # Removes the value key from the elements list and maintains heap properties.
        if not self.contains(key):
            return

        index = self.elements.index(key)
        self.swap(index, len(self.elements) - 1)
        self.elements.pop()
        self.heapifyDown(index)

    def heapifyDown(self, i: int):
        # Heapification process after deletion.
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.elements) and self.elements[left] > self.elements[largest]:
            largest = left
        if right < len(self.elements) and self.elements[right] > self.elements[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapifyDown(largest)

    def heapifyUp(self, i: int):
        # Heapification process after insertion.
        while i > 0 and self.elements[self.parent(i)] < self.elements[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, array):
        # Takes in an array of values and returns a valid max heap.
        for i in range(len(array) // 2, -1, -1):
            self.elements = array.copy()
            self.heapifyDown(i)
        return self.elements
