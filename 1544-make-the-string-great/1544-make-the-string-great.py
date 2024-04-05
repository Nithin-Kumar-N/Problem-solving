class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()  # Remove the last character if it makes a bad pair
            else:
                stack.append(char)  # Otherwise, add the character to the stack
        
        return ''.join(stack)