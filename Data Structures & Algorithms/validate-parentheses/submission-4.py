class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i in s:
            if i in hash_map:
                stack.append(i)
            elif(stack and hash_map[stack[-1]] == i):
                stack.pop()
            else:
                return False
        return len(stack) == 0
