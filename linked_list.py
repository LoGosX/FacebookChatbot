

class ClosedList:
    def __init__(self, size):
        self._head = 0
        self._tail = 0
        self._items = []
        self._size = size
        self._num_of_elements = 0

    @property
    def max_size(self):
        return self._size

    @property
    def size(self):
        return self._num_of_elements
    
    def append(self, value):
        if self._num_of_elements < self._size:
            self._num_of_elements += 1
            self._items.append(value)
        else:
            self._head = (self._head + 1) % self._size
            self._tail = (self._tail + 1) % self._size
            self._items[self._head] = value
    
    def __getitem__(self, key):
        return self._items[(self._tail + key) % self._num_of_elements]