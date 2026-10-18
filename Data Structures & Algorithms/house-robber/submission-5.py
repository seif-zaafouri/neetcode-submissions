from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def best(k):
            # Maximum money from the first k houses.
            if k == 0:
                return 0
            if k == 1:
                return nums[0]

            skip = best(k - 1)
            take = nums[k - 1] + best(k - 2)

            return max(skip, take)

        return best(len(nums))