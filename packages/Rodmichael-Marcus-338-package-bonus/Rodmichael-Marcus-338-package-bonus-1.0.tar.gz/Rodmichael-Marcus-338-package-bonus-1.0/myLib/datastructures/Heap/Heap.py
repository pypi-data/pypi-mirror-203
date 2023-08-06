class Heap:
    def __init__(self, size=None, array=None):
        # Initialize the elements list, either empty or with a given size or array.
        self.elements = []
        if size is not None:
            self.elements = [None] * size
        elif array is not None:
            self.elements = self.heapify(array)

    def getSize(self) -> int:
        # Returns the size of the elements list.
        return len(self.elements)

    def isEmpty(self) -> bool:
        # Returns True if the elements list is empty, False otherwise.
        return len(self.elements) == 0

    def clear(self):
        # Clears the elements of the list.
        self.elements = []

    def contains(self, i: int) -> bool:
        # Returns True if the value i is in the elements list, False otherwise.
        return i in self.elements

    def insert(self, key: int):
        # Placeholder for inserting a value into the heap.
        pass

    def delete(self, key: int):
        # Placeholder for deleting a value from the heap.
        pass

    def sort(self):
        # Sorts the elements in the heap using the heap property.
        sorted_elements = []
        original_elements = self.elements.copy()
        while not self.isEmpty():
            self.swap(0, len(self.elements) - 1)
            sorted_elements.append(self.elements.pop())
            self.heapifyDown(0)
        self.elements = original_elements
        return sorted_elements

    def print(self):
        # Prints the content of the elements list with parent indices and elements on separate lines.
        if self.isEmpty():
            print("Heap is empty.")
            return

        level = 0
        i = 0
        while i < len(self.elements):
            level_length = 2 ** level
            parent_indices = " ".join(str((i - 1) // 2) for i in range(i, i + level_length))
            elements = " ".join(str(e) for e in self.elements[i:i + level_length])
            print(parent_indices)
            print(elements)
            i += level_length
            level += 1

    def parent(self, i: int) -> int:
        # Returns the index of the parent of the element at index i.
        return (i - 1) // 2

    def left(self, i: int) -> int:
        # Returns the index of the left child of the element at index i.
        return 2 * i + 1

    def right(self, i: int) -> int:
        # Returns the index of the right child of the element at index i.
        return 2 * i + 2

    def swap(self, x: int, y: int):
        # Swaps the elements at indices x and y.
        self.elements[x], self.elements[y] = self.elements[y], self.elements[x]

    def heapifyDown(self, i: int):
        # Placeholder for the heapification process after deletion.
        pass

    def heapifyUp(self, i: int):
        # Placeholder for the heapification process after insertion.
        pass

    def heapify(self, array):
        # Placeholder for converting an array into a valid heap.
        pass
