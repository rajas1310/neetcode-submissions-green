class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stack = []
        for c in s:
            if c in "})]":
                if not stack: return False
                if d[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return True if not len(stack) else False