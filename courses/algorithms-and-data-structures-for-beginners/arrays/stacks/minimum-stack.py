# Minimum Stack
# 
# Design a stack class that supports the push, pop, top, and 
# getMin operations.
#
# -MinStack() initializes the stack object.
# -void push(int val) pushes the element val onto the stack.
# -void pop() removes the element on the top of the stack.
# -int top() gets the top element of the stack.
# -int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.
#
# Example 1:
#
# Input: ["MinStack", "push", 1, "push", 2, "push", 0,
#         "getMin", "pop", "top", "getMin"]
#
# Output: [null,null,null,null,0,null,2,1]
#
# Explanation:
#   MinStack minStack = new MinStack();
#   minStack.push(1);
#   minStack.push(2);
#   minStack.push(0);
#   minStack.getMin(); // return 0
#   minStack.pop();
#   minStack.top();    // return 2
#   minStack.getMin(); // return 1
#
# Constraints:
#   -2^31 <= val <= 2^31 - 1.
#   pop, top and getMin will always be called on non-empty stacks.


# class MinStack:

#     def __init__(self):
#         self.stack = []
        

#     def push(self, val: int) -> None:
#         self.stack.append(val)
    

#     def pop(self) -> None:
#         self.stack.pop()


#     def top(self) -> int:
#         return self.stack[-1]
        

#     def getMin(self) -> int:
#         sorted_stack = sorted(self.stack)
#         return sorted_stack[0]


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:

        # we store encoded values of the difference between
        # the pushed value and the current minimum
        if not self.stack:
            # append 0 since its val - val
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            # update minimum if necessary
            if val < self.min:
                self.min = val
    
    def pop(self) -> None:
        if not self.stack:
            return

        encoded = self.stack.pop()

        # if this was negative, it was the minimum
        # for example:
        #   push(4) -> [0], min 4
        #   push(2) -> [0, -2(2-4)], min 2
        #   push(3) -> [0, -2, 1(3-2)], min 2
        #   pop() -> [0, -2], min 2
        #   pop() -> [0], min 0(2 - (-2))
        if encoded < 0:
            # 0 = 2 - (-2)
            self.min = self.min - encoded


    def top(self) -> int:
        top_encoded = self.stack[-1]
        
        if top_encoded > 0:
            return top_encoded + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
