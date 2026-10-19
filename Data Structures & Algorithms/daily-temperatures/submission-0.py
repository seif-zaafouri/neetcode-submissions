class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0 for _ in range(n)]
        stack = []
        t = temperatures

        for i in range(n - 1, -1, -1):
            while stack and t[stack[-1]] <= t[i]:
                stack.pop()

            if stack:
                output[i] = stack[-1] - i

            stack.append(i)

        return output