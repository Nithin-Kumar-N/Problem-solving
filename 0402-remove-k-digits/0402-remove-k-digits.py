class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k is still greater than zero, remove remaining digits from the end of the stack
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        while stack and stack[0] == '0':
            stack.pop(0)

        # If the stack is empty, return '0'
        if not stack:
            return '0'

        # Convert the stack to a string and return
        return ''.join(stack)

        