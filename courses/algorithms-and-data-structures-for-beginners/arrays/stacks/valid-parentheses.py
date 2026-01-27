# Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
# Input: s = "[]"
# Output: true
#
# Example 2:
# Input: s = "([{}])"
# Output: true
#
# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.
#
# Constraints:
#
# 1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        stack = []

        for c in s:
            if stack != [] and c in parentheses_map and parentheses_map[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

            # print(f"letter = {c}, stack = {stack}")

        if stack == []:
            return True
        else:
            return False

