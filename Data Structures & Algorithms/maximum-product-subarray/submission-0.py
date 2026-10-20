class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for x in nums[1:]:
            new_max = max(
                x,
                x * current_max,
                x * current_min
            )

            new_min = min(
                x,
                x * current_max,
                x * current_min
            )

            current_max = new_max
            current_min = new_min

            result = max(result, current_max)
        
        return result