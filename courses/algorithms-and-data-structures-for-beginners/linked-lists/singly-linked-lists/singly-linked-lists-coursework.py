# Design Singly Linked List
#
# Design a Singly Linked List class.
#
# Your LinkedList class should support the following operations:
# - LinkedList() will initialize an empty linked list.
# - int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
# - void insertHead(int val) will insert a node with val at the head of the list.
# - void insertTail(int val) will insert a node with val at the tail of the list.
# - bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
# - int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
#
# Example 1:
# Input: 
# ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
# Output:
# [null, null, null, true, [0, 2]]
#
# Example 2:
# Input:
# ["insertHead", 1, "insertHead", 2, "get", 5]
# Output:
# [null, null, -1]
#
# Note:
# The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
class LinkedList:

    # we need the list node quest
    class ListNode:
        def __init__(self, val, next = None):
            self.next = None
            self.val = val


    # LinkedList() will initialize an empty linked list.
    def __init__(self):
        self.head = self.ListNode(-1)   # fake value of -1
        self.tail = self.head
        self.length = 0


    # int get(int i) will return the value of the ith node 
    # (0-indexed). If the index is out of bounds, return -1.
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        i = 0
        cur = self.head
        
        while cur:

            if i == index:
                return cur.val
            else:
                cur = cur.next
                i += 1

        return cur.val


    # void insertHead(int val) will insert a node with 
    # val at the head of the list.
    def insertHead(self, val: int) -> None:
        # create new node
        new_node = self.ListNode(val)
        # assign this new nodes next pointer to point at the current head
        new_node.next = self.head
        # then assign classes head to this node
        self.head = new_node

        # if linked list was empty, point the tail to this new head
        if self.length == 0:
            self.tail = new_node
        
        self.length += 1


    # void insertTail(int val) will insert a node with val 
    # at the tail of the list.
    def insertTail(self, val: int) -> None:
        # create the new node
        new_node = self.ListNode(val)
        # assign previous tails next pointer to this new node, new tail doesn't have a next
        self.tail.next = new_node
        # then we correct the class tail to this node
        self.tail = new_node

        # if the linked list was empty, point the head to this new node
        if self.length == 0:
            self.head = new_node

        self.length += 1


    # bool remove(int i) will remove the ith node (0-indexed).
    # If the index is out of bounds, return false, otherwise 
    # return true.
    def remove(self, index: int) -> bool:
        if index >= self.length or self.length == 0:
            return False

        # start at head and iterate until index
        i = 0
        cur = self.head

        # once we're the node before the index to remove
        while i < index - 1:
            cur = cur.next
            i += 1

        # when we break out, cur will have been assigned to the node right before index 

        # remove the node ahead of cur
        if cur == self.head and index == 0:
            self.head = cur.next
        else:
            if cur and cur.next:
                
                if cur.next == self.tail:
                    self.tail = cur
                cur.next = cur.next.next
        
        self.length -= 1

        return True


    # int[] getValues() return an array of all the values in the 
    # linked list, ordered from head to tail.
    def getValues(self) -> List[int]:
        if self.length == 0:
            return []

        values = []

        cur = self.head
        
        while cur != self.tail:
            values.append(cur.val)
            cur = cur.next

        values.append(cur.val)
        
        return values
