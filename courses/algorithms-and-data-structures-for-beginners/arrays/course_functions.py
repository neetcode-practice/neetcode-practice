# Traversing through an array

my_array = [1,2,3]

for i in range(len(my_array)):
    print(my_array[i])
    
# OR

i = 0
while i < len(my_array):
    print(my_array[i])
    i += 1
    
# Deleting from the end of the array
def removeEnd(arr: list, length: int) -> list:
    if length > 0:
        # Overwrite with a 0
        arr[length - 1] = 0
        
# Delete at ith index
def removeIthIndex(arr: list, i: int, length: int) -> list:
    for j in range(i + 1, length):
        # overwrite i and shift all values left 1
        arr[j - 1] = arr[j]

# Inserting at the end
def insertAtEnd(arr, val, length, capacity):
    # simply insert at length
    if length < capacity:
        arr[length] = val
        
# def insertAtEnd(arr, val, capacity):
#     n = len(arr)
#     # simply insert at length
#     if n < capacity:
#         arr[n] = val

# Insert at ith index
def insertAtIth(arr, i, val, length):
    # shift everything from i 1 spot right and insert
    
    # loop from last index (length - 1) to i since i - 1 isn't included by range function 
    for j in range(length - 1, i - 1, -1):
        arr[j + 1] = arr[j]
        
    arr[i] = val