# Dynamic Array 

class DynamicArray:
    
    #  initialize an empty array with a capacity of capacity, where capacity > 0.
    def __init__(self, capacity: int):
        # Initialize array variables used below
        if capacity > 0:
            self.capacity = capacity        
            self.arr = [0] * self.capacity
        else:
            self.capacity = 0
            self.arr = []
        
        self.length = 0
    
    # return the element at index i. Assume that index i is valid.
    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]

    # set the element at index i to n. Assume that index i is valid.
    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.arr[i] = n

    # Insert n in the last position of the array:
    def pushback(self, n) -> None:
        if self.length == self.capacity:
            self.resize()
        
        # Insert at the last element
        self.arr[self.length] = n
        self.length += 1
        
    # pop and return the element at the end of the array. Assume that the array is non-empty.
    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        
        return self.arr[self.length]
        
    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity
        
        # Copy elements to newArr
        for i in range(len(self.arr)):
            newArr[i] = self.arr[i]
        
        # Assign the self array as the new array
        self.arr = newArr
        
    def getSize(self) -> int:
        return self.length        
    
    def getCapacity(self) -> int:
        return self.capacity