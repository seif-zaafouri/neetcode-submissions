class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def least(a):
            if a in memo:
                return memo[a]

            best = float("inf")

            for c in coins:
                if c <= a:
                    candidate = 1 + least(a - c)
                    best = min(best, candidate)

            memo[a] = best
            return best

        result = least(amount)
        return -1 if result == float("inf") else result