class Solution:
    def isValid(self, s: str) -> bool:
        """
        s = ( [ { } ] )
        stack = '(' | LIFO
        hmap = {'[':']', '{': '}'}
        iterations:
        - s = '(' | c='[' | ']' not in stack
        - s = '([' | c='{' | '}' not in stack
        - s = '([{' | c='}' | '{' in stack -> s='(['
        - s = '([' | c=']' | '[' in stack -> s='('
        - s = '(' | c=')' | '(' in stack -> s=''
        """
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []

        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True