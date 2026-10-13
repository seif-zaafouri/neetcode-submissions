class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in ['{', '[','(']:
                stack.append(b)
            else:
                if not stack or stack.pop() != mapping[b]:
                    return False
        return (stack == [])