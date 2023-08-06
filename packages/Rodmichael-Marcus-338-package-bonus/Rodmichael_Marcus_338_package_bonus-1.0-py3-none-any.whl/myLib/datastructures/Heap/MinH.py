from .Heap import Heap

class MinHeap(Heap):
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
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.elements) and self.elements[left] < self.elements[smallest]:
            smallest = left
        if right < len(self.elements) and self.elements[right] < self.elements[smallest]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapifyDown(smallest)

    def heapifyUp(self, i: int):
        # Heapification process after insertion.
        while i > 0 and self.elements[self.parent(i)] > self.elements[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, array):
        # Takes in an array of values and returns a valid min heap.
        for i in range(len(array) // 2, -1, -1):
            self.elements = array.copy()
            self.heapifyDown(i)
        return self.elements
