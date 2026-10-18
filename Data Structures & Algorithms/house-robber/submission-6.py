class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def best(k):
            if k == 0:
                return 0
            if k == 1:
                return nums[0]

            if k not in memo:
                memo[k] = max(
                    best(k - 1),
                    nums[k - 1] + best(k - 2)
                )

            return memo[k]

        return best(len(nums))