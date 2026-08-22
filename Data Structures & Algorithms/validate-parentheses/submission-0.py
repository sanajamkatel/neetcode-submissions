class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing_to_opening = {')': '(',
                            '}': '{',
                            ']':'['}
        
        for char in s:
            if char in closing_to_opening:
                if not stack:
                    return False
                top = stack.pop()
                 
                if closing_to_opening[char] != top:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0



        