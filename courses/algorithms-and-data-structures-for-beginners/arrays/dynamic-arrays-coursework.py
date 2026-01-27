# Dynamic Array Insertion

class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity
        
        # Copy elements to newArr
        for i in range(self.arr):
            newArr[i] = self.arr[i]
        
        # Assign the self array as the new array
        self.arr = newArr

    # Insert n in the last position of the array:
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        
        # Insert at the last element
        self.arr[self.length] = n
        self.length += 1