class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[t] = number of ordered sequences summing to t
        # base case:
        dp = [0] * (target+1)
        dp[0] = 1
        # dp[t] = sum(dp(t-x)) for x in nums and x <= t
        for t in range(1, target+1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t-num]
        return dp[target]
